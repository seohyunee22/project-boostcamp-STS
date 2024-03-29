![header](https://capsule-render.vercel.app/api?type=waving&height=200&fontSize=50&color=gradient&text=KLUE-STS&fontAlignY=26&desc=문장%20간%20의미%20유사도%20측정(Semantic%20Text%20Similarity,%20STS)&descAlignY=49&descSize=23&fontColor=ffffff)
<td style="text-align:center; border-color:white" rowspan="3" width=660>
      <p align="center">
        <img src="/etc/klue-sts-img.png" width=600>    
      </p>
    </td>  

### <p align="center"><code>KLUE-STS task</code>는</p>
<p align="center">복수 문장에 대한 유사도를</p>
<p align="center">선형적 수치로 제시하는 NLP Task 입니다. </p>

<table align="center">
  <tr height="8px">
    <td align="center" style="text-align:center;" width="80px">
      <b>Notion</b>
    </td>
    <td align="center" style="text-align:center;" width="80px">
      <b>Wrap-up Report</b>
    </td>
  </tr>
  
  <tr height="40px">
    <td align="center" width="150px">
       <a href="https://www.notion.so/mayy2yy/STS-Project-f0e582c9af364fbda2681693a73bf7c5"><img src="https://img.shields.io/badge/notion-%23000000.svg?&style=flat-square&logo=notion&logoColor=white "/></a>
    </td>
    <td align="center" width="150px">
      <a href="/assets/STS_WrapUp_NLP_09.pdf"><img src="https://img.shields.io/badge/PDF-CC2927?style=flat-square&logo=microsoft&logoColor=white">
    </td>
  </tr>
</table>
<p align="center">(↑ 로고를 클릭하면 링크로 이동합니다)</p>
<br>

## 📖 Overview
### 1. 프로젝트 개요
인간은 **교정작업**을 하면서 의미적으로 중복된 문장을 인지하고 수정하게 됩니다.
<br>
그렇다면 기계의 경우는, 서로 구조적으로 다르지만 **의미가 유사한 것을 어떻게 구별**할 수 있을까요?
<br>
이러한 경우에 `Semantic Text Similiarity(STS)` Task를 사용할 수 있습니다.
<br>

<code>STS</code>는 TE(Textual Entailment)와 달리 **수치화 가능한 양방향 동등성**을 가정하고 진행됩니다.
<br>
따라서 **STS Task는 정보 추출, 질문-답변 및 요약과 같은 NLP 작업 전반에 널리 활용 및 응용**되고 있습니다.

### 2. 목표
- STS 데이터셋을 활용해 <code>두 문장의 유사도를 측정하는 AI 모델을 구축</code>하는 것을 대회의 목표로 합니다.
- [0, 5] 범위의 유사도 점수를 예측하는 것을 목적으로 합니다.

### 3. 데이터셋 
- 학습 데이터셋 9,234개, 검증 데이터셋 550개, 평가 데이터셋 1,100개 로 구성되어 있습니다.
- 평가 데이터의 50%는 Public 점수 계산에 활용, 실시간 리더보드에 반영되며 남은 50%는 Private 결과에 반영되어 최종평가에 반영됩니다.


### 4. 평가 방법
평가 방법은 다음과 같습니다.
<br>

1. 입력(.csv)을 구축한 모델을 활용한 유사도 측정 완료 후, ID와 0~5사이의 유사도 점수를 출력(.csv)으로 제출
- `입력`: 두 개의 문장과 ID, 유사도 정보
- `출력`: 평가 데이터에 있는 각 문장쌍에 대한 ID와 0~5 사이의 유사도 점수
  

<td style="text-align:center; border-color:white" rowspan="3" width=660>
      <p align="center">
        <img src="/etc/pearson.png" width=400>    
      </p>
</td>  
<br>

2. 평가 기준

- 평가 기준은 예측과 정답 간의 `피어슨 상관 계수(Pearson Correlation Coefficient)` 입니다.
- 따라서, 개별 예측값과 정답값의 일치보다는 전체적인 경향의 유사도가 중요합니다.
<br>
  



##  🙆🏻 Members 
<table align="center">
  <tr height="8px">
    <td align="center" style="text-align:center;" width="190px">
      <b>공통</b>
    </td>
    <td align="center" style="text-align:center;" width="760px">
      <b>데이터 분석, 실험 수립 및 진행, 하이퍼 파라미터 튜닝, Wrap Up 리포트 작성</b>
    </td>
  </tr>
</table>
<table align="center">
  <tr height="155px">
    <td align="center" width="190px">
      <a href="https://github.com/seohyunee22"><img src="https://avatars.githubusercontent.com/seohyunee22"/></a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/in-sukim"><img src="https://avatars.githubusercontent.com/in-sukim"/></a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/Secludor"><img src="https://avatars.githubusercontent.com/Secludor"/></a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/"><img src="https://avatars.githubusercontent.com/nachalsa"/></a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/Yunan31"><img src="https://avatars.githubusercontent.com/Yunan31"/></a>
    </td>
  </tr>
  
  <tr height="40px">
    <td align="center" width="190px">
      <a href="https://github.com/seohyunee22">양서현_T6099</a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/">김인수</a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/sanggank">오주영</a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/tmdqor">문지원</a>
    </td>
    <td align="center" width="190px">
      <a href="https://github.com/nachalsa">손윤환</a>
    </td>
  </tr>

   <tr height="80px">
    <td style="text-align:left;" width="190px">
      - EDA<br>
      - 데이터 증강<br>(Label Smoothing, Copied Sentence)<br>
      - 문장 교정<br>(py-hanspell)<br> 
    </td>
    <td style="text-align:left;" width="190px">
      - 앙상블 Baseline <br>코드 작성<br>
      - 데이터 증강(Bert) <br>
    </td>
    <td style="text-align:left;" width="190px">
      - 손실함수 탐색<br>
      - 손실함수 비교/분석<br>/최적화<br>
    </td>
    <td style="text-align:left;" width="190px">
      - 한국어 기반 모델 탐색<br>
      - 데이터 전처리 실험(특수문자 제거, 형태소 분석)<br>
    </td>
    <td style="text-align:left;" width="190px">
      - 한국어 기반 모델 탐색<br>
      - 데이터 이상치 분석<br>
      - 데이터 증강(역번역)<br>
    </td>
  </tr>
</table>
<!--
### <p align="center">협업관리</p>
<table align="center">
  <tr height="8px">
    <td align="center" style="text-align:center;" width="80px">
      <b>Notion</b>
    </td>
    <td align="center" style="text-align:center;" width="80px">
      <b>Github</b>
    </td>
  </tr>
  
  <tr height="40px">
    <td align="center" width="150px">
       <a href="https://www.notion.so/Time-Flies-ae9378d5426d4e659ee3b5aacaab0d64"><img src="https://img.shields.io/badge/notion-%23000000.svg?&style=flat-square&logo=notion&logoColor=white "/></a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/seohyunee22/project-boostcamp-STS/blob/main/etc/STS_WrapUp_NLP_09.docx"><img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white">
    </td>
  </tr>
</table>
<p align="center">(↑ 로고를 클릭하면 링크로 이동합니다)</p>
<br>
-->
<br>
            
## 🛠️ Tech Stack
<img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat-square&logo=Pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Pytorch Lightening-792EE5?style=flat-square&logo=lightning&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"> 
<br><img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/notion-%23000000.svg?&style=flat-square&logo=notion&logoColor=white "/>

<!--<img src="https://img.shields.io/badge/jupyter notebook-F37626?style=flat-square&logo=jupyter&logoColor=white"> -->
<!--<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">-->
<!--<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">-->
<br>

  

## 💡 프로젝트 수행

<table align="center">
 <tr height="40px">
    <td align="center" style="text-align:center;" width="250px">
      <b>01</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>02</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>03</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>04</b>
    </td>
  </tr>
  <tr height="50px">
    <td align="center" style="text-align:center;" width="250px">
      <b>EDA</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Data pre/post processing</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Loss Function</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Model</b>
    </td>
  </tr>
  <tr height="100px">
    <td align="left" style="text-align:left;" width="260px">
      - Basic Data Information <br>
      - Label, Source 분포<br>
      - 문장 길이 분석<br> 
      - 문장 형태 분석<br> 
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - Data Cleaning<br>(py-haanspell, regexp) <br>
      - Data Augmentation<br>(K-TACC, Label Smoothing, Copied Sentence)<br>
      - Inference output 결과 분석
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - SmoothL1Loss <br>
      - MSELoss<br>
      - General and Adaptive Robust</b><br> 
      - MSE + Huber/noise/pearson<br> 
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - kykim/electra-kor-base <br>
      - snunlp/KR-ELECTRA-discriminator<br>
      - monologg/koelectra-base-v3-discriminator<br> 
      - Ensemble<br> 
    </td>
  </tr>
</table>
<br>

  
  

## 결과
- 최종 제출: Soft Ensemble { <code>kykim(증강)</code>, <code>snu</code>, <code>snu(증강)</code>, <code>monologg</code>, <code>snu(aug+hanspell)</code> }
- Public Score <code>0.9285</code> / Private Score <code>0.9349</code>

 학습 데이터와 검증 데이터의 분포의 차이를 줄이는 것, 모델의 Inference 결과를 분석하여 편향된 Inference 경향을 줄이는 것에 집중하여 대회를 진행하였습니다.<br>
 맞춤법 · 띄어쓰기 교정 및 Label Smoothing & Copied Sentence 활용한 데이터 증강을 통해 단일 모델 SOTA 달성 (Pearson: 0.9098) 하였습니다.<br>
 또한 모델의 Soft Ensemble을 통해 일반화 성능을 높이고, 편향된 Inference 경향을 줄이는 데 성공했습니다.<br>
 하지만 앙상블에 대한 이해도가 높지 않아, 최종 제출한 앙상블 모델보다 제출하지 않은 앙상블 모델이 더 좋은 결과를 내어 아쉬운 결과를 얻었습니다.


![](https://lh7-us.googleusercontent.com/VmXqjdu10k6ahP2OVH15BkhWjaE37zaxtL-KLmpgDTjw6lANDux25JGj7IqH76mX6UPpeWLRp4DFrS76Qhd8uEmopwImRYSTq2Yi7CRVyZB3-24mJ8yC_JJUBBgYDt9SDK-_-gco1uKQvMds5e_UsKc)

  



## Appendix

### 실험결과 정리

- loss = <code>SmoothL1</code>, batch_size = <code>16</code> 고정
  
| Data | Model | epoch | lr | val_loss | val_pearson |
| --- | --- | --- | --- | --- | --- |
| baseline | snunlp/KR-ELECTRA-discriminator | 10 | 1.7e-05 | 0.18286 | 0.91436 |
| swap | snunlp/KR-ELECTRA-discriminator | 10 | 1.7e-05 | 0.05068 | 0.9137 |
| regexp | snunlp/KR-ELECTRA-discriminator | 10 | 1.7e-05 | 0.18286 | 0.91436 |
| swap+regexp | kykim/electra-kor-base | 10 | 1.7e-05 |  | 0.90356 |
| hanspell | snunlp/KR-ELECTRA-discriminator | 11 | 1.7e-05 | 0.19808 | 0.920 |
| aug(no drop) | snunlp/KR-ELECTRA-discriminator | 10 | 1.896e-05 | 0.17166 | 0.92171 |
| aug(no drop) | kykim/electra-kor-base | 10 | 1.896e-05 | 0.14737 | 0.92098 |
| aug(1/3 drop) | snunlp/KR-ELECTRA-discriminator | 15 | 1.896e-05 |  | 0.9167 |
| aug+smoothing(label0 1/4)+copied(hanspell) | snunlp/KR-ELECTRA-discriminator | 9 | 1.7e-05 | 0.15111 | 0.9326 |
| aug+smoothing(label0 1/4)+copied(hanspell) | kykim/electra-kor-base | 15 | 1.7e-05 | 0.15504 | 0.92406 |
| aug+smoothing(label0 1/4)+copied(hanspell) | monologg/koelectra-base-discriminator | 10 | 1.7e-05 | 0.18699 | 0.89659 |
| aug+smoothing(label0 1/2)+copied(hanspell) | snunlp/KR-ELECTRA-discriminator | 9 | 1.7e-05 | 0.15137 | 0.92763 |
| aug+smoothing(label0 1/2)+copied(hanspell) | kykim/electra-kor-base | 15 | 1.7e-05 | 0.14123 | 0.92443 |

  
### 손실함수 정리
| 모델 | 손실함수 | Pearson Score |  |  |
| --- | --- | --- | --- | --- |
|  |  | Valid | Public | Private |
| jhgan/ko-sroberta-multitask | SmoothL1Loss | 0.89 | 0.8808 | 0.9043 |
|  | GARL | 0.8920 | 0.8614 | 0.8844 |
|  | MSE | 0.9104 | 0.8827 | 0.9153 |
|  | MSE+Huber | 0.9093 | 0.8756 | 0.8968 |
|  | MSE+noise | 0.9066 | 0.8831 | 0.9072 |
|  | MSE+pearson | 0.9080 | 0.8802 | 0.9002 |
| snunlp/KR-ELECTRA-discriminator | SmoothL1Loss | 0.9307 |  |  |
|  | MSE+Huber | 0.9245 |  |  |
| kykim/electra-kor-base | SmoothL1Loss | 0.9017 |  |  |
|  | MSE | 0.9057 |  |  |
|  | MSE+Huber | 0.8820 |  |  |


