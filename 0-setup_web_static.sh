#!/usr/bin/env bash
# Install Nginx if not already installed
# Create necessary folders if they don't exist
# Create a fake HTML file
# Create or recreate symbolic link
# Update Nginx configuration
# Restart Nginx
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
web="<html>
  <head>
  </head>
  <body>
    <p>Test Nginx Configuration</p>
  </body>
</html>"
echo "$web" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
