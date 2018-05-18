from pwn import *
import string
import time
from base64 import *
r = remote('localhost',33333)

def xor(s1,s2):
	return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2)])

def repeat(string, len_cipher):
    return (string*(int(len_cipher/len(string))+1))[:len_cipher]

def getCipher():
	r.recv()
	r.send('1\n')
	r.recv()
	r.send('1234\n')
	return r.recv().split(':')[1].strip()

# len(b64_d(cookie)) = 64*n + len(padding) (padding % 4 == 0)
# finding 4bytes last of b64_d(cookie) at which block 4 bytes of padding
# if return at block 0 means len(b64_d(cookie)) = 64*n + 4
# when XORing with key(length 64) 4 bytes last is XORing with key[0:4]
# brute-forcing to find valid bytes key which will valid '}' at the at of plain(json format)
# continue finding key[4:8] key[8:12] until full key 
def getBlock():
	b64 = getCipher()
	b64 = b64decode(b64)
	s = b64[(len(b64)/64)*64:]
	b = len(s)/4 -1
	if b == -1:
		b = b + 16
	return b, b64[-4:]

# create an array to brute for finding suitable char base on 4 bytes last
b64arr = []
for i in string.printable:
	b64arr.append(b64encode(i+'"}'))
b64arr.append(b64encode('}'))
b64arr.append(b64encode('"}'))

# using each char in arr to find valid char base on another cipher
def check(arr,block):
	while True:
		# choose another block
        	b2, c2 = getBlock()
        	if b2 == block and c2 != c1:
                	break

	lst_char = []
	for char in arr:
		try:
			key = xor(c1,char)
			check = b64decode(xor(key,c2))
			if len(check) == 1 and check == '}':
				lst_char.append(char)
			if len(check) == 2 and check == '"}':
				lst_char.append(char)
			if len(check) == 3 and '"}' in check:
				lst_char.append(char)
		except:
			pass
	return lst_char

# finding full key
key = ''
for block in range(0,16): 
	# just get one block for constant
	while True:
		b1, c1 = getBlock()
       		if b1 == block:
       			break
	# getting first array from check func
	lst_char = check(b64arr,block)
	# loop until return array from check func is unique
	while True:
		lst = check(lst_char,block)
		if len(lst) == 1:
			break
	# convert char to 4bytes key
	unique_key = xor(lst[0],c1)
	key += unique_key
	print key

# we have key. the last part is so easy
cipher = getCipher()
cipher = cipher.decode('base64')
key = repeat(key,len(cipher))
plain = xor(cipher,key)
plain = plain.decode('base64')

print 'Found!!!! Plaintext is: ', plain









