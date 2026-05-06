# 使用node:20-alpine映像檔作為基底
FROM node:20-alpine

# 維護者資訊
LABEL maintainer="hueyan"

# 指定工作目錄
WORKDIR /app

# 複製專案的檔案至工作目錄
COPY . .

# 在工作目錄使用package.json檔案安裝套件
RUN npm install

# 指定容器監聽的埠號
EXPOSE 3000

# 啟動容器時執行的命令
CMD ["node", "app.js"]

