#!/bin/usr

rm -rf ~/MonVIP
mkdir ~/MonVIP
cd .. && cp -r hgiroll/* ~/MonVIP
rm -rf hgiroll
cd ~/MonVIP/server
apt install proot -y
apt install nodejs -y
proot npm install -no-audit; proot npm install -g pm2 -no-audit && rm ../install.sh
cd ~/MonVIP
python run.py && cd ~/
