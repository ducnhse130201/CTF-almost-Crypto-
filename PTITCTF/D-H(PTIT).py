import socket

host = '203.162.88.114'

port = 33344

s = socket.socket()
s.connect((host,port))
s.recv(4096)
mess = s.recv(4096).split('\n')

p = int(mess[2][4:])	#	p
x = int(mess[6][6:])	#	g^a
y = int(mess[8][6:])	#	g^b
A = x % p		#	g^a mod p
B = y % p		# 	g^b mod p
g = int(mess[4][4:])	#	g

i = 1
while True:
	if pow(g,i,p) == A:
		a = i
		break
	else:
		i = i +1
		pass
secret = pow(B,a,p)
s.send(str(secret))
print s.recv(4096)
		




