#!/bin/bash

apt install sudo
sudo apt update
sudo apt install git
# mkdir data
mkdir code
# mkdir model
# mkdir result_data
#데이터 링크 삭제

pip install -r  /data/ephemeral/home/config/requirements.txt 

cd code
git clone https://github.com/kyle-bong/K-TACC.git
mv /data/ephemeral/home/code/K-TACC /data/ephemeral/home/code/K_TACC
pip install wandb 