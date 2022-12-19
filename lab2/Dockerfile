FROM php:5-apache
WORKDIR /var/www/html
COPY src/ .
COPY ./php.ini "$PHP_INI_DIR/conf.d/"
RUN mkdir /var/www/html/uploads && chmod 777 /var/www/html/uploads