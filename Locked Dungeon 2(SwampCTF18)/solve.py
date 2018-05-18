from telnetlib import *
from base64 import *
import string
from hashlib import *

alpha = string.uppercase + string.lowercase + string.digits


def xor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

host,port = 'chal1.swampctf.com',1460

# Bit flipping to pass lv1
ori = 'send_modflag_enc'
change = 'get_modflag_md5A'


while True:

	r = Telnet(host,port)
	cipher = r.read_until('\n').strip()
	cipher = b64decode(cipher)
	a = r.read_until('\n').strip()
	print a

	ori_iv = cipher[:16]
	ori_c = cipher[16:]

	mod_iv = xor(xor(change,ori), ori_iv)
	mod_cipher = b64encode((mod_iv + ori_c))

	print 'Input payload: ' + mod_cipher 
	r.write(mod_cipher+'\n')
	a = r.read_until('\n').strip()

	print a
	if a[:21] == 'Dungeon goes deeper..':
		len_c = len(cipher)
		break

print '\n'
print '\t\tBit flipping successfuly ... '
print '\t\tStart pwning to get the flag!!! '
print '\n'

# Bit flipping the last char of plaintext
# base on function: unpad = lambda inp: inp[:-ord(inp[-1])]
# flipping last char of plaintext which has value acssi 0-255

len_enc_mod_flag = len(mod_cipher)
inp_size_limit = int(len_enc_mod_flag*4/3) + 50

# create a md5 list
allmd5hashes = []

for i in range(256):
	new_enc = b64encode(cipher + 'a'*15 + chr(i) + 'a'*16)
	r.write(new_enc+'\n')
	a = r.read_until('\n').strip()
	allmd5hashes.append(a)

# finding flag from the md5 list
flag = ''

while True:
	for char in range(256):
		testflag = flag + chr(char)
		if b64encode(md5(testflag).digest()) in allmd5hashes:
			print testflag
			flag = testflag
			break
	if flag[-1] == '}':
		print 'Flag: ' + flag
		break
























