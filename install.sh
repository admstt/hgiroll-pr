#!/bin/usr

rm -rf ~/MonVIP
mkdir ~/MonVIP
cd .. && cp -r hgiroll-pr/* ~/MonVIP
rm -rf hgiroll-pr
cd ~/MonVIP/server
apt install proot -y
apt install nodejs -y
proot npm install -no-audit; proot npm install -g pm2 -no-audit && cd .. && rm -rf install.sh
python run.py
cd ~/
ls
