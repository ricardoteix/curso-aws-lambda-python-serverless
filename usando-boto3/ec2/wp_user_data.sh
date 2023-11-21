#!/bin/bash

sudo apt update
sudo apt install apache2 -y
sudo ufw allow 'Apache'

sudo apt install php-curl php-gd php-mbstring php-xml php-xmlrpc php-soap php-intl php-zip -y
sudo apt install mysql-server -y
sudo apt install php-mysql -y
sudo su
echo "<VirtualHost *:80> <Directory /var/www/html/>AllowOverride All</Directory> </VirtualHost>" > /etc/apache2/sites-available/wordpress.conf
sudo a2enmod rewrite

sudo apt-get install php libapache2-mod-php -y

sudo echo "<?php phpinfo();" | sudo tee /var/www/html/info.php

wget -c http://wordpress.org/latest.tar.gz
tar -xzvf latest.tar.gz
sudo mv wordpress/* /var/www/html/
sudo mv /var/www/html/index.html /var/www/html/apache.html
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/

sudo systemctl restart apache2