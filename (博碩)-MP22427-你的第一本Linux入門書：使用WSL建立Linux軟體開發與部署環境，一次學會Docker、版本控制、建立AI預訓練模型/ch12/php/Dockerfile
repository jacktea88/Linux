# 使用官方的 PHP 7.2 Apache 映像檔
FROM php:7.2-apache

# 定義維護者
LABEL maintainer="hueyan"

# 指定工作目錄
WORKDIR /var/www/html/

# 複製專案的 www 子目錄至工作目錄
COPY ./www/ .

# 指定容器埠號為 80
EXPOSE 80
