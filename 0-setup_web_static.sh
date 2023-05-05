#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static.

# install nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

# craetes dir /data/web_static/releases
# if it does not exist
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# prints message to file
sudo echo "Welcome to michael website" | sudo tee /data/web_static/releases/test/index.html

# creates symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# changes ownership of data
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location \/hbnb_static {\n\talias \/data\/web_static\/current\/;\n}' /etc/nginx/sites-enabled/default
sudo service nginx restart
