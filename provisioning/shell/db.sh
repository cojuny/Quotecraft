#!/bin/bash
DATABASE_PASS='admin123'

sudo mv /vagrant/mariadb.repo /etc/yum.repos.d/
sudo yum repolist
sudo yum install mariadb-server -y
sudo systemctl start mariadb
sudo systemctl enable mariadb

sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
sudo firewall-cmd --reload

sudo mysqladmin -u root password "$DATABASE_PASS"
sudo mysql -u root -p"$DATABASE_PASS" -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('admin123'); FLUSH PRIVILEGES;"
sudo mysql -u root -p"$DATABASE_PASS" -e "grant all privileges on quotes.* TO 'root'@'%' identified by '$DATABASE_PASS'"
sudo mysql -u root -p"$DATABASE_PASS" -e "create database quotes"
sudo mysql -u root -p"$DATABASE_PASS" quotes < /vagrant/quotes.sql
sudo mysql -u root -p"$DATABASE_PASS" -e "FLUSH PRIVILEGES"

sudo systemctl restart mariadb