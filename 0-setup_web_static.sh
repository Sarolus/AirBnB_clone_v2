#!/usr/bin/env bash
# Sets up a web server for the deployment of the web static.
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "38i\ \tlocation \/hbnb_static {\n\t\alias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
