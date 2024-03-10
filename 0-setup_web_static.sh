#!/usr/bin/env bash
# This script sets up web servers for deploying the web_static content.

echo -e "\e[1;32m Starting the setup process...\e[0m"

# Update system packages
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m System packages updated.\e[0m"
echo

# Configure firewall to allow incoming NGINX HTTP connections
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Firewall configured to allow NGINX HTTP connections.\e[0m"
echo

# Create necessary directories for web_static
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "\e[1;32m Directories created for web_static deployment.\e[0m"
echo

# Add a test string to the index.html file
echo "<h1>Holberton School</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test string added to the index.html file.\e[0m"
echo

# Prevent overwrite by checking if the /data/web_static/current path exists
if [ -d "/data/web_static/current" ]; then
    echo "Path /data/web_static/current already exists."
    sudo rm -rf /data/web_static/current;
fi
echo -e "\e[1;32m Overwrite prevention in place.\e[0m"
echo

# Create a symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
echo -e "\e[1;32m Symbolic link created to the test release.\e[0m"
echo

# Configure NGINX to serve the web_static content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;32m NGINX configuration updated and symbolic link created.\e[0m"
echo

# Restart NGINX to apply changes
sudo service nginx restart
echo -e "\e[1;32m NGINX restarted successfully.\e[0m"
