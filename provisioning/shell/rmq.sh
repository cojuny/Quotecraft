sudo yum update -y
sudo yum install wget epel-release -y
sudo rpm -Uvh /vagrant/erlang-solutions-1.0-1.noarch.rpm
sudo yum install erlang socat logrotate -y
sudo rpm --import https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo rpm -Uvh /vagrant/rabbitmq-server-3.8.35-1.el8.noarch.rpm
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server

sudo setsebool -P nis_enabled 1

sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --add-port=5671/tcp --permanent
sudo firewall-cmd --add-port=5672/tcp --permanent
sudo firewall-cmd --reload

sudo sh -c 'echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config'
sudo rabbitmqctl add_user test test
sudo rabbitmqctl set_user_tags test administrator

sudo systemctl restart rabbitmq-server
nohup sleep 10 &&  reboot &
echo "going to reboot now"