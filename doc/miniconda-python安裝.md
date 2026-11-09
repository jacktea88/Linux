# miniconda

## 安裝miniconda

**可用一般user帳號安裝**

**注意：下載連結以官網最新的網址為準**

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh

## 新增Miniconda環境變數(手動設定, 若選自動初始化(init)設定，此步不用做)

nano ~/.bashrc

export PATH=/home/your-user-name/miniconda3/bin:$PATH

## 讓環境變數配置生效(記得要執行, 須出現(base))

source ~/.bashrc

## 檢查conda是否可啟動，且show版本

conda --version

# AI Keras NLP install

## 建立env (須指定用python 3.10 for tensorflow)

conda create -n keras-nlp python=3.10

conda activate  XXX

## install 相關套件

pip install --upgrade keras
pip install tensorflow (v2.15以後不支援windows)(檔案較大須先安裝)
pip install notebook
pip install gradio
pip install ipywidgets (可能不支援)
pip install keras-nlp (檔案較大須先安裝)

## 啟動jupyter notebook

### 建立設定檔(run指令才會出現設定檔)

jupyter notebook --generate-config

#### 修改設定檔

檔案位置：~/.jupyter/jupyter_notebook_config.py

修改設定：(注意：設定項目前面不能有空格)

c.ServerApp.token =''

#(免token登入, 註：兩個單引號，中間是空的字元)

c.ServerApp.ip ='0.0.0.0'

#(可遠端登入)

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

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

sudo apt install pkg-config default-libmysqlclient-dev build-essential python3-dev

## VENV安裝mysqlclient

pip install mysqlclient

### 如果mysql版本不是最新版

出現下面的error：
django.db.utils.NotSupportedError: MySQL 8.4 or later is required (found 8.0.46).

原因：目前的 Django 是 6.1.3，這個版本的 MySQL 後端最低要求是 MySQL 8.4；你的資料庫是 8.0.46，所以會拋出 NotSupportedError。

最快可行的修復有兩條路：

一、升級 MySQL 到 8.4 或更新
二、把 Django 降到 5.2.x（通常是教學環境最省事）

### Django 降到 5.2.x

python -m pip uninstall -y django
python -m pip install "Django>=5.2,<5.3"

## 建立資料表

python manage.py migrate

## 安裝其他requirement

pip install -r requirements.txt

### save to requirements.txt

pip freeze > requirements.txt

## 啟動server

* 注意：setting的SQL HOST要改成127.0.0.1
  python manage.py runserver 0.0.0.0:8000

# Node.js 安裝

sudo apt install nodejs
sudo apt install npm

## 安裝lite-server
npm install lite-server

Node.js 22 安裝（給 Node-RED）
Node-RED 目前需要 Node.js v22.9 或更新版本。
不要用 apt install nodejs（通常版本太舊）。

方法一：nvm（建議，一般使用者最方便）
安裝 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

重新載入 shell
source ~/.bashrc

安裝並啟用 Node.js 22
nvm install 22
nvm alias default 22
nvm use 22

確認版本（需 >= v22.9）
node -v
npm -v

方法二：NodeSource（系統層安裝）
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v
npm -v

安裝 Node-RED
npm install -g --unsafe-perm node-red

啟動 Node-RED
node-red

預設瀏覽器網址：
http://your-linux-ip:1880

常見問題
如果升級後還是看到 v18.19.1，代表目前 shell 還在用舊路徑：

關閉並重開終端機
再執行 nvm use 22
重新檢查 node -v
