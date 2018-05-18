import string

c2n = dict(zip(string.uppercase+string.lowercase+string.digits,range(64)))

n2c = dict(zip(range(64),string.uppercase+string.lowercase+string.digits))

cipher = 'o1AwoBQ4rBQSnlkCnmXvsF0DpRQxnmc0bCXvpmbvomwypmg4q1rw'

text = ''
for i in range(len(cipher)):
	num = c2n[cipher[i]] - 15
	if num < 0:
		num = num + 64
	text += n2c[num]

print text.decode('base64')
'''
# crypto1.py

from base64 import b64encode, b64decode

import string

from secret import key, flag



c2n = dict(zip(string.uppercase+string.lowercase+string.digits,range(64)))

n2c = dict(zip(range(64),string.uppercase+string.lowercase+string.digits))



flag = b64encode(flag)



ciphertext = ''.join(n2c[(c2n[c] + key) % 64] for c in flag)

print ciphertext


#o1AwoBQ4rBQSnlkCnmXvsF0DpRQxnmc0bCXvpmbvomwypmg4q1rw
'''
