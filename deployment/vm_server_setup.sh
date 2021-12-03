# as root
adduser butla
usermod -a -G sudo butla
mkdir /var/www

# as butla over ssh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx

# Add nginx config.
# "server" declaration using SSL needs to be commented out for initializing certbot.
# TODO add my config as under /etc/nginx/sites-available instead of in the main config

# create venv for bultrowicz.com
sudo apt install python3.8-venv
python3 -m venv blog_venv
./blog_venv/bin/pip install -r bultrowicz.com/requirements.txt

# add certbot/letsencrypt
# follows https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# uncomment ssl server configuration in /etc/nginx/nginx.conf

# add other users:
# - borsuk, with sudo
# - rynek
#
# Add `www` folder in their HOME. Their sitename and index.html
# Add their public key to /home/$USER/.ssh/authorized_keys
