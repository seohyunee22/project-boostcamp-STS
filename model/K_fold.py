import argparse
import random

import pandas as pd

from tqdm.auto import tqdm

import transformers
import torch
import torchmetrics
import pytorch_lightning as pl
import re
# Wandb
from pytorch_lightning.loggers import WandbLogger
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.callbacks.early_stopping import EarlyStopping


from sklearn.model_selection import KFold
#from module.seed import seed_everything

import warnings

# 경고 제거
transformers.logging.set_verbosity_error()
warnings.filterwarnings("ignore", ".*does not have many workers.*")
warnings.filterwarnings("ignore", ".*TensorBoard support*")
warnings.filterwarnings("ignore", ".*target is close to zero*")

# seed 고정
torch.manual_seed(0)
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)
random.seed(1234)


class Dataset(torch.utils.data.Dataset):
    def __init__(self, inputs, targets=[]):
        self.inputs = inputs
        self.targets = targets

    # 학습 및 추론 과정에서 데이터를 1개씩 꺼내오는 곳
    def __getitem__(self, idx):
        # 정답이 있다면 else문을, 없다면 if문을 수행합니다
        if len(self.targets) == 0:
            return torch.tensor(self.inputs[idx])
        else:
            return torch.tensor(self.inputs[idx]), torch.tensor(self.targets[idx])

    # 입력하는 개수만큼 데이터를 사용합니다
    def __len__(self):
        return len(self.inputs)


class Dataloader(pl.LightningDataModule):
    def __init__(self, model_name, batch_size, shuffle, train_path, dev_path, test_path, predict_path, seed_value, num_splits, k):
        super().__init__()
        self.model_name = model_name
        self.batch_size = batch_size
        self.shuffle = shuffle

        self.train_path = train_path
        self.dev_path = dev_path
        self.test_path = test_path
        self.predict_path = predict_path

        self.train_dataset = None
        self.val_dataset = None
        self.test_dataset = None
        self.predict_dataset = None

        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name, max_length=160) # 100
        self.target_columns = ['label']
        self.delete_columns = ['id']
        self.text_columns = ['sentence_1', 'sentence_2']

        #kfold
        self.seed = seed_value
        self.num_splits = num_splits
        self.k = k

    def tokenizing(self, dataframe):
        data = []
        for idx, item in tqdm(dataframe.iterrows(), desc='tokenizing', total=len(dataframe)):
            # 두 입력 문장을 [SEP] 토큰으로 이어붙여서 전처리합니다.
            text = '[SEP]'.join([item[text_column] for text_column in self.text_columns])
            outputs = self.tokenizer(text, add_special_tokens=True, padding='max_length', truncation=True)
            data.append(outputs['input_ids'])
        return data

    def preprocessing(self, data, is_train=False):
        # 안쓰는 컬럼을 삭제합니다.
        data = data.drop(columns=self.delete_columns)

        # 타겟 데이터가 없으면 빈 배열을 리턴합니다.
        try:
            targets = data[self.target_columns].values.tolist()
        except:
            targets = []
        # 텍스트 데이터를 전처리합니다.
        inputs = self.tokenizing(data)

        return inputs, targets

    def setup(self, stage='fit'):
        if stage == 'fit':
            # 학습 데이터와 검증 데이터셋을 호출합니다
            train_data = pd.read_csv(self.train_path)
            val_data = pd.read_csv(self.dev_path)

            data = pd.concat([train_data, val_data], ignore_index=True)

            kf = KFold(n_splits=self.num_splits, shuffle=self.shuffle, random_state=self.seed)
                
            train_datas = []
            val_datas = []
            
            for t, v in kf.split(data):
                train_datas.append(data.iloc[t].reset_index())
                val_datas.append(data.iloc[v].reset_index())

            train_inputs, train_attention_masks, train_token_type_ids, train_targets = self.preprocessing(train_datas[self.k], is_train=True)
            val_inputs, val_attention_masks, val_token_type_ids, val_targets = self.preprocessing(val_datas[self.k])
        
            self.train_dataset = Dataset(train_inputs, train_attention_masks, train_token_type_ids, train_targets)
            self.val_dataset = Dataset(val_inputs, val_attention_masks, val_token_type_ids, val_targets)

            self.train_sampler = self.get_sampler(train_targets)
            
        else:
            # 평가데이터 준비
            self.test_dataset = self.val_dataset

            predict_data = pd.read_csv(self.predict_path)
            predict_inputs, predict_targets = self.preprocessing(predict_data)
            self.predict_dataset = Dataset(predict_inputs, [])

    def train_dataloader(self):
        return torch.utils.data.DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=args.shuffle)

    def val_dataloader(self):
        return torch.utils.data.DataLoader(self.val_dataset, batch_size=self.batch_size)

    def test_dataloader(self):
        return torch.utils.data.DataLoader(self.test_dataset, batch_size=self.batch_size)

    def predict_dataloader(self):
        return torch.utils.data.DataLoader(self.predict_dataset, batch_size=self.batch_size)


class Model(pl.LightningModule):
    def __init__(self, model_name, lr):
        super().__init__()
        self.save_hyperparameters()

        self.model_name = model_name
        self.lr = lr

        # 사용할 모델을 호출합니다.
        self.plm = transformers.AutoModelForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path=model_name, num_labels=1)
        # Loss 계산을 위해 사용될 L1Loss를 호출합니다.
        self.loss_func = torch.nn.SmoothL1Loss()
        self.drop = torch.nn.Dropout(p = 0.4)
    
    def forward(self, x):
        x = self.plm(x)['logits']

        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = self.loss_func(logits, y.float())
        self.log("train_loss", loss)

        return loss

    def validation_step(self, batch, batch_idx): # 이상치 찾아보기 !!!!!!
        x, y = batch
        logits = self(x)
        loss = self.loss_func(logits, y.float())
        self.log("val_loss", loss)

        self.log("val_pearson", torchmetrics.functional.pearson_corrcoef(logits.squeeze(), y.squeeze()))

        return loss

    def test_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)

        self.log("test_pearson", torchmetrics.functional.pearson_corrcoef(logits.squeeze(), y.squeeze()))

    def predict_step(self, batch, batch_idx):
        x = batch
        logits = self(x)

        return logits.squeeze()

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), weight_decay=0.3 ,lr=self.lr)
        return optimizer


if __name__ == '__main__':
    # 하이퍼 파라미터 등 각종 설정값을 입력받습니다
    # 터미널 실행 예시 : python3 run.py --batch_size=64 ...
    # 실행 시 '--batch_size=64' 같은 인자를 입력하지 않으면 default 값이 기본으로 실행됩니다
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', default='kykim/electra-kor-base', type=str)
    # xlm-roberta-large / Bi-directional GRU adding / monologg/koelectra-base-v3-discriminato / snunlp/KR-ELECTRA-discriminator / kykim/electra-kor-base
    parser.add_argument('--batch_size', default=16, type=int)
    parser.add_argument('--max_epoch', default=15, type=int)  # 15~20 정도만
    parser.add_argument('--shuffle', default=True)
    parser.add_argument('--learning_rate', default=1.7e-05, type=float)
    parser.add_argument('--train_path', default='./v4_train.csv')
    parser.add_argument('--dev_path', default='./dev.csv')
    parser.add_argument('--test_path', default='./dev.csv')
    parser.add_argument('--predict_path', default='./test.csv')

    parser.add_argument('--wandb_project', default='level1_STS')
    #kfold
    #parser.add_argument('--kfold', default=0, type=int)
    parser.add_argument('--seed', default=1234, type=int)
    parser.add_argument('--nums_fold', default=5, type=int)
    args = parser.parse_args()

    
    pl.seed_everything(1234)

    for k in range(args.nums_fold):
        dataloader = Dataloader(args.model_name, args.batch_size, args.shuffle, args.train_path, args.dev_path,
                            args.test_path, args.predict_path, args.seed, args.nums_fold, k)
        # TRAIN 
        model = Model(args.model_name, args.learning_rate)
    
        model_name_ch = re.sub('/','_',args.model_name)
        wandb_logger = WandbLogger(
                name=f'{model_name_ch}_{args.batch_size}_{args.learning_rate}_v3',
                project=args.wandb_project,
                )

        # callback
        early_stop_callback = EarlyStopping(
            monitor='val_pearson',
            min_delta=0.001,
            patience=5,
            verbose=True,
            mode='max'
            )
        
        checkpoint_callback = ModelCheckpoint(
            monitor='val_pearson',  # Monitor the validation Pearson coefficient
            mode='max',             # Mode 'max' because you want to maximize this metric
            save_top_k=1,           # Save only the top 1 model
            filename='f{model_name_ch}{epoch}-{val_pearson:.2f}',  # Filename includes epoch and metric
            verbose=True,
            dirpath = './model/'
        )
        
        trainer = pl.Trainer(
            accelerator="gpu", 
            logger=wandb_logger,    # W&B integration
            devices=1, 
            max_epochs=args.max_epoch, 
            log_every_n_steps=1,
            callbacks = [early_stop_callback, checkpoint_callback]
        )

        # Train part
        trainer.fit(model=model, datamodule=dataloader)
        test_pearson = trainer.test(model=model, datamodule=dataloader)[0]['test_pearson']

        torch.save(model, './version_4/output_v4_kfold.pt')