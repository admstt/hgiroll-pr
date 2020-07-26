#!/usr/bin/python3

import os, time


os.system('clear')
try:
	print('[+] checking ip forwarder')
	time.sleep(2)
	os.system("ip addr show tun0 |grep -oP '(?<=inet\s)[\da-f.:]+' >ip")
	ip=open('ip')
	myIP=ip.read().rstrip()
	myIP == " "
	monvip=("http://"+myIP+":22533/login")
	if not myIP:
		print('[x] IP forwarder Not Connected.')
		exit()
	else:
		print('[*] IP forwarder Connected')
		print('[+] starting MonVIP')
		os.system("cd server;proot pm2 delete all >logs;proot pm2 start index.js > logs & xdg-open "+(monvip))
except:
	time.sleep(2)
	print('[!] You must to activate OpenVPN first ')
	exit()

