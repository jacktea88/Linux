
------------------------------
## Docker 部署 MySQL Server 指令集 (Ubuntu)## 1. 安裝 Docker (若尚未安裝)

sudo apt update


## 2. 下載 MySQL 官方映像檔

# 下載最新版本
sudo docker pull mysql:latest

## 3. 啟動 MySQL 容器 (基本版)
此指令會啟動一個名為 mysql-server 的容器，並將容器的 3306 埠對應到主機的 3306 埠。

sudo docker run --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=你的密碼 \
  -p 8888:3306 \
  -d mysql:latest

## 4. 啟動 MySQL 容器 (進階持久化版)
強烈建議： 使用 -v 掛載主機目錄，避免容器刪除時資料遺失。

sudo docker run --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=你的密碼 \
  -v /home/user/mysql_data:/var/lib/mysql \
  -p 3306:3306 \
  -d mysql:latest

## 5. 常用管理指令

* 進入資料庫終端機：

sudo docker exec -it mysql-server mysql -u root -p

* 查看運行狀態：

sudo docker ps

* 停止 / 啟動容器：

sudo docker stop mysql-server
sudo docker start mysql-server

* 查看容器日誌 (排錯用)：

sudo docker logs mysql-server

# 使用 Docker Compose 
好處是可以用一個設定檔 (.yaml) 管理所有參數，之後只需一行指令就能啟動或停止，非常適合長期維運。

以下是建置步驟：
## 1. 建立專案目錄
先建立一個資料夾來存放設定檔：

mkdir mysql-docker
cd mysql-docker

## 2. 建立 docker-compose.yml
使用你喜歡的編輯器（如 nano 或 vim）建立檔案：

nano docker-compose.yml

將以下內容貼上（請自行修改 MYSQL_ROOT_PASSWORD）：

services:
  db:
    image: mysql:latest
    container_name: mysql-server
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: 你的密碼
      MYSQL_DATABASE: my_database
      MYSQL_USER: user
      MYSQL_PASSWORD: user_password
    ports:
      - "3306:3306"
    volumes:
      - ./mysql_data:/var/lib/mysql
  phpmyadmin:
    image: phpmyadmin:latest
    container_name: phpmyadmin
    restart: always
    links:
      - db
    environment:
      PMA_HOST: db
      PMA_PORT: 3306
      PMA_ARBITRARY: 1
    ports:
      - "8080:80"

## 3. 啟動服務
在該目錄下執行：

sudo docker compose up -d
* -d 表示在背景執行

MySQL 位址： localhost:3306phpMyAdmin 
網頁介面： 開啟瀏覽器輸入 http://localhost:8080
伺服器(Server)： db (或是填入 MySQL 容器名稱)
帳號： root
密碼： 你在 MYSQL_ROOT_PASSWORD 設定的內容

## 4. 常用管理指令 (Docker Compose)

* 停止並移除容器： sudo docker compose down
* 重啟服務： sudo docker compose restart
* 查看日誌： sudo docker compose logs -f
* 進入資料庫： sudo docker exec -it mysql-server mysql -u root -p

------------------------------
提示：
使用 Docker Compose 時，資料會自動存放在當前目錄下的 mysql_data 資料夾內，方便備份與移植。



