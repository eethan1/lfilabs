FROM php:7.2-apache
WORKDIR /var/www/html
RUN apt-get update && apt-get install inotify-tools -y
COPY src/ .
COPY ./php.ini "$PHP_INI_DIR/conf.d/"
RUN mkdir /var/www/html/uploads && chmod 777 /var/www/html/uploads