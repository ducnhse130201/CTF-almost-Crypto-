from telnetlib import *
from base64 import *
from hashlib import *
r = Telnet('localhost', 40000)

real = 'aoot++++++++++++'
change = 'root*+++++++++++'
name = '\x00' * 16

def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))

r.read_until('Your choice: ')
r.write('1')
r.read_until('Name: ')
r.write(name + '\n')
r.read_until('Username: ')
r.write(real + '\n')
r.read_until('Cookie: ')
ct = r.read_until('\n').strip()
ct = b64decode(ct)

iv = ct[:16]
iv2 = md5(ct[16:32]).digest()
iv3 = md5(ct[32:48]).digest()

payload = XOR(XOR(change, iv2), iv3)

r.read_until('Your choice: ')
r.write('1')
r.read_until('Name: ')
r.write(name + '\n')
r.read_until('Username: ')
r.write(real + payload + '\n')
r.read_until('Cookie: ')
cookie = r.read_until('\n').strip()
cookie = b64decode(cookie)

exploit = iv + ct[16:32] + cookie[48:64] + ct[48:]
exploit = b64encode(exploit)

r.read_until('Your choice: ')
r.write('2')
r.read_until('Cookie: ')
r.write(exploit + '\n')
r.read_until('This is flag: ')
flag = r.read_until('\n')
print 'FLAG: ' + flag






