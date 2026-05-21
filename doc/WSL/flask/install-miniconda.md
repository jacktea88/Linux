# miniconda

## 安裝miniconda

wget https://repo.anaconda.com/miniconda/Miniconda3-1atest-Linux-x86_64.64.sh

bash Miniconda3-1atest-Linux-x86_64.64.sh

## 新增Miniconda環境變數(手動設定)

nano ~/.bashrc

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
pip install tensorflow (v2.15以後不支援windows)(檔案較大須先安裝)
pip install notebook
pip install gradio
pip install ipywidgets
pip install keras-nlp (檔案較大須先安裝)

## 啟動jupyter notebook

### 建立設定檔

jupyter notebook --generate-config

#### 修改設定檔

檔案位置：~/.jupyter/jupyter_notebook_config.py

修改設定：

c.ServerApp.token =''  (免token登入)

c.ServerApp.ip ='0.0.0.0' (可遠端登入)

jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser

# Flask

## 開發環境建立

conda create -n flask python=3.10

conda activate flask

pip install flask

python3 -m flask run

**python manage.py runserver **0.0**.**0.0**:**8000

無法遠端連線
