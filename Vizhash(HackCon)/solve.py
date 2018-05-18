from PIL import Image
import itertools
from hashlib import *
import string
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def sum_to_n(n):
	sum = 0
	for i in range(1,n+1,1):
		sum += i
	return sum
		
def encode(s):
	return ''.join([ chr(ord(c)+4) for c in s[::-1] ])
def decode(s):
	return ''.join([ chr(ord(c)-4) for c in s[::-1] ])

img = Image.open('digest.png')

pixels = list(img.getdata())
pixels_lst = pixels[:12936]	# filter (R,G,B) > 128

# brute-forcing every char in encryted_flag base on encrypt func
def encrypt(char):
	lst = []
	m = md5(char).hexdigest()
	m = int(m,16)
	m = str(hex(m))
	for j in range(0, len(m)-3, 3):
		lst.append((128 + ord(m[j])^ord(m[j+1]), 128 + ord(m[j+1])^ord(m[j+2]), 128 + ord(m[j+2])^ord(m[j+3])))
	return lst

encrypted_flag = ''
# checking every block of 11 pairs (R,G,B) in pixels_lst with encrypt(char) if compare -> TRUE: that's the correct char
for i in range(0,len(pixels_lst),11):
	lst = pixels_lst[i:i+11]
	for j in string.printable:
		if compare(lst,encrypt(j)):
			encrypted_flag += j
		else:
			pass
# Now calculating the len(b64_flag)
i = 1
while True:
	if sum_to_n(i) == len(encrypted_flag):
		break
	i += 1		
# And we know that encrypted_flag[-len(b64_flag):] is b64_flag
enc = encrypted_flag[-i:]
enc = decode(enc)	# decode it
print 'Found!!! Flag is: ' + enc.decode('base64')

	
		



