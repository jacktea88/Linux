---
------------------------------
## Docker 部署 MySQL Server 指令集 (Ubuntu)
## 1. 安裝 Docker (若尚未安裝)

### 記得做
sudo apt update
### 搜尋：docker ubuntu install
### 網址：
https://docs.docker.com/engine/install/ubuntu/

## 2. 下載 MySQL 官方映像檔

# 下載最新版本

sudo docker pull mysql:latest

## 3. 啟動 MySQL 容器 (基本版)

此指令會啟動一個名為 mysql-server 的容器，並將容器的 3306 埠對應到主機的 8888 埠。

sudo docker run --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=你的密碼 \
  -p 8888:3306 \
  -d mysql:latest

## 4. 啟動 MySQL 容器 (進階持久化版)

強烈建議： 使用 -v 掛載主機目錄，避免容器刪除時資料遺失。

sudo docker run --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=你的密碼 \
  -v /home/jack/mysql_data:/var/lib/mysql \
  -p 8888:3306 \
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

使用編輯器（如 nano 或 vim）建立檔案：

nano docker-compose.yml

將以下內容貼上（請自行修改 MYSQL_ROOT_PASSWORD & port）：

services:
  db:
    image: mysql:8.4
    container_name: mysql-server
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: my_database
      MYSQL_USER: user
      MYSQL_PASSWORD: user_password
    ports:
      - "8888:3306"
    volumes:
      - ./mysql_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin:latest
    container_name: phpmyadmin
    restart: always
    depends_on:
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

MySQL 位址： localhost:8888

phpMyAdmin
網頁介面： 開啟瀏覽器輸入 http://localhost:8080
伺服器(Server)： db (或是填入 MySQL 容器名稱)
帳號： root/user
密碼： 你在 MYSQL_ROOT_PASSWORD 設定的內容

------------------------------
提示：
使用 Docker Compose 時，資料會自動存放在當前目錄下的 mysql_data 資料夾內，方便備份與移植。

## 4. 常用管理指令 (Docker Compose)

* 將user帳號加入到docker群組(不須sudo就可執行docker)： 
sudo usermod -aG docker user帳號
newgrp docker (讓新設定值生效)
* 停止並移除容器： sudo docker compose down
* 重啟服務： sudo docker compose restart
* 查看日誌： sudo docker compose logs -f
* 進入資料庫： sudo docker exec -it mysql-server mysql -u root -p

### 常用操作指令
* 啟動docker：sudo systemctl start docker
* 停止docker：sudo systemctl stop docker
* 重啟docker：sudo systemctl restart docker
* 查看docker狀態：sudo systemctl status docker
* 查看docker日誌：sudo journalctl -u docker

### 映像檔管理指令
* 提取映像檔：sudo docker pull 映像檔名稱[:tag]
* 刪除映像檔：sudo docker rmi <image_id>
* 刪除映像檔：sudo docker rm 映像檔名稱[:tag]
* 列出映像檔：sudo docker images

### 容器管理指令
* 列出所有容器：sudo docker ps -a
* 停止容器：sudo docker stop <container_id> or <container_name>
* 強制關閉：sudo docker kill <container_id> or <container_name>
* 啟動容器：sudo docker start <container_id> or <container_name>
* 刪除容器：sudo docker rm <container_id> or <container_name>
* 列出容器：sudo docker ps
* 啟動容器：sudo docker run -d -p 3306:3306 --name mysql-server mysql:latest

### 其他指令
* 查看Docker版本：sudo docker version
* 查看Docker狀態：sudo docker info
* 查看Docker服務狀態：sudo systemctl status docker
* 查看Docker日誌：sudo journalctl -u docker
* 查看Docker網路狀態：sudo docker network ls
* 查看Docker儲存區狀態：sudo docker volume ls

### hub管理指令
* 搜尋映像檔：docker search <映像檔名稱>
* 下載映像檔：docker pull <映像檔名稱>
* 刪除映像檔：docker rmi <映像檔名稱>
* 列出映像檔：docker images
* 提交映像檔：docker commit <容器名稱> <映像檔名稱>[:tag]
* 標記映像檔：docker tag <local映像檔名稱>[:tag] <hub映像檔名稱>[:tag]
* 推送映像檔：docker push <hub映像檔名稱>[:tag]

### 網路管理指令
* 創建網路：sudo docker network create <網路名稱>
* 刪除網路：sudo docker network rm <網路名稱>
* 列出網路：sudo docker network ls


# 補充：建立其他web server
docker run --name websrv -d -p 9090:80 nginx
docker exec -it websrv bash
docker cp index.html websrv:/usr/share/nginx/html
---

# push to hub 流程
docker ps
docker commit websrv myimage:latest
docker images
docker tag myimage:latest jacktea88/myimage:latest
docker login
docker push jacktea88/myimage:latest
docker rmi jacktea88/myimage:latest
docker run --name websrv-hub -p 9595:80 jacktea88/myimage:latest

