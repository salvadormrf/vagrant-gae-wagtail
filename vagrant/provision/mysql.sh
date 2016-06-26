#!/bin/bash

PROJECT_NAME=$1

MYSQL_ROOT_PASSWORD=root
MYSQL_VERSION=5.5

DATABASE_NAME=$PROJECT_NAME
DATABASE_USER=$PROJECT_NAME
DATABASE_PASS=$PROJECT_NAME

# Install mysql and give password to installer
export DEBIAN_FRONTEND=noninteractive
debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD"

apt-get install mysql-server-$MYSQL_VERSION mysql-client libmysqlclient-dev -y

echo "Creating new database $DATABASE_NAME";
mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CREATE USER '$DATABASE_USER'@'%' IDENTIFIED BY '$DATABASE_PASS';"
mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE $DATABASE_NAME CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL ON $DATABASE_NAME.* TO '$DATABASE_USER'@'%' IDENTIFIED BY '$DATABASE_PASS';"

# Change bind address to allow connections from anywhere
sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf

# Restart the sql service
sudo service mysql restart
