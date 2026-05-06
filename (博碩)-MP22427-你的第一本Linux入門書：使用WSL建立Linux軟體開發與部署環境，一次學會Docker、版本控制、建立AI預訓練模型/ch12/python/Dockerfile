# 使用python:3.10-alpine映像檔作為基底
FROM python:3.10-alpine

# 維護者資訊
LABEL maintainer="hueyan"

# 指定工作目錄
WORKDIR /app

# 在工作目錄安裝flask
RUN pip install flask

# 複製專案的檔案至工作目錄
COPY . .

# 指定容器監聽的埠號
EXPOSE 8080

# 啟動容器時執行的命令
CMD ["python", "app.py"]
