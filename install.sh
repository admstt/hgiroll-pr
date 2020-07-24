#!/bin/usr

rm -rf ~/MonVIP
cp -r ../admstt/hgiroll ~/MonVIP
cd ~/MonVIP/server
apt install proot -y
proot apt install nodejs -y
proot npm install -no-audit; proot npm install -g pm2 & rm ../install.sh
