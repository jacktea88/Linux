# miniconda
## 安裝miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-1atest-Linux-x86_64.64.sh

## 新增Miniconda環境變數
export PATH=/home/your-user-name/miniconda3/bin:$PATH

## 讓環境變數配置生效
source ~/.bashrc

## 檢查conda是否可啟動，且show版本
conda --version

# Keras NLP install

## 建立env (須指定用python 3.10 for tensorflow)
conda create -n keras-nlp python=3.10

## install 相關套件
pip install --upgrade keras
pip install tensorflow
pip install notebook
pip install gradio
pip install ipywidgets
pip install keras-nlp

## 啟動jupyter notebook
jupyter notebook --no-browser
