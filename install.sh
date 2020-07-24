#!/bin/usr

apt install proot -y
cd ~/MonVIP/server
proot apt install nodejs -y
proot npm install -no-audit; proot npm install -g pm2 & rm ../install.sh
