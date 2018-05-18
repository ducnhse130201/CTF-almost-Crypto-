import socket
from base64 import *
from hashlib import *
import string
def readuntil(conn, e):
    buf = bytes()
    while not buf.decode().endswith(e):
        buf += conn.recv(1)
    return buf
def payload(s):
    if len(s) < 43:
        p = socket.socket()
        p.connect(('localhost',33337))
        readuntil(p,': ')
     	p.send( '\n')	
     	readuntil(p,': ')
     	p.send( s + '\n')
     	message = p.recv(1024).split(': ')[1].strip()
     	p.close()
     	return b64decode(message)
    else:
	p = socket.socket()
        p.connect(('localhost',33337))
        readuntil(p,': ')
     	p.send( s[:43] +'\n')	
     	readuntil(p,': ')
     	p.send( s[43:] + '\n')
     	message = p.recv(1024).split(': ')[1].strip()
     	p.close()
     	return b64decode(message)




flag = ''
for i in range(69):
	n = 69 - i
	grep = payload(n*'a')[0:80]
	for char in string.printable:
		guess = payload(n*'a' + flag + char)[0:80]
		if guess == grep:
			flag += char
			print flag
			break
	if flag[-1] == '}':
		break









		
		

