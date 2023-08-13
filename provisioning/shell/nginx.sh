# adding repository and installing nginx		
apt update
apt install nginx -y
cat <<EOT > webapp
upstream webapp {

  server dj01:8000;
  server dj02:8000;

}

server {
  
  listen 80;

location /static/ {
  proxy_pass http://webapp;
  
}

location / {

  proxy_pass http://webapp;

}

}

EOT

mv webapp /etc/nginx/sites-available/webapp
rm -rf /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/webapp /etc/nginx/sites-enabled/webapp

#starting nginx service and firewall
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

systemctl start nginx
systemctl enable nginx
systemctl restart nginx