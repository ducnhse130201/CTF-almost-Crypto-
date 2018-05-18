from hashlib import *
import random
import itertools
h = 'f528a6ab914c1ecf856a1d93103948fe'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ{}'
cipher = 'LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ'
format_flag = 'SECCON{'

def repeat(a,len_b):
    return (a*(int(len_b/len(a))+1))[:len_b]

def decode_vigenere(cipher,key,alpha):
	if len(key) < len(cipher):
		key = repeat(key,len(cipher))
	plain = ''
	for i in range(len(cipher)):
		num = alpha.index(cipher[i]) - alpha.index(key[i])
		if num < 0:
			num = num + len(alpha)
		plain += alpha[num]
	return plain


key = 'VIGENERE'
possible_keys = [''.join(i) for i in itertools.product(alpha,repeat = 4)]

for c in possible_keys:
	key = key + c
	plaintext = decode_vigenere(cipher,key,alpha)
	if md5(plaintext).hexdigest() == h:
		print plaintext
		break
	key = 'VIGENERE'
		
		
