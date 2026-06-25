# miniconda

## 安裝miniconda

**注意：下載連結以官網最新的網址為準**

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.64.sh

## 新增Miniconda環境變數(手動設定, 若選自動設定，此步不用做)

nano ~/.bashrc

export PATH=/home/your-user-name/miniconda3/bin:$PATH

## 讓環境變數配置生效(記得要執行, 須出現(base))

source ~/.bashrc

## 檢查conda是否可啟動，且show版本

conda --version

# AI Keras NLP install

## 建立env (須指定用python 3.10 for tensorflow)

conda create -n keras-nlp python=3.10

## install 相關套件

pip install --upgrade keras
pip install tensorflow (v2.15以後不支援windows)(檔案較大須先安裝)
pip install notebook
pip install gradio
pip install ipywidgets (可能不支援)
pip install keras-nlp (檔案較大須先安裝)

## 啟動jupyter notebook

### 建立設定檔

jupyter notebook --generate-config

#### 修改設定檔

檔案位置：~/.jupyter/jupyter_notebook_config.py

修改設定：

c.ServerApp.token =''

#(免token登入, 註：兩個單引號，中間是空的字元)

c.ServerApp.ip ='0.0.0.0'

#(可遠端登入)

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser

在win10的流灠器：http://your-linux-ip:8888

#### 在vscode執行jupyter notebook

一、使用ssh連線

二、右上角選conda執行環境

python環境->建立python環境->輸入解譯器路徑：

miniconda3/envs/{conda環境名稱}/bin/python

# Flask(無法遠端連線)

## 開發環境建立

conda create -n flask python=3.10

conda activate flask

pip install flask

python3 -m flask run

無法遠端連線

# Django(可遠端連線)
## 如果要用到mysql，須另安裝相關依賴套件
sudo apt update

sudo apt install \
pkg-config \
default-libmysqlclient-dev \
build-essential \
python3-dev

## 安裝其他requirement
pip install -r requirements.txt

## 啟動server
* 注意：setting的SQL HOST要改成127.0.0.1 
python manage.py runserver 0.0.0.0:8000

# Node.js 安裝
sudo apt install nodejs
sudo apt install npm

