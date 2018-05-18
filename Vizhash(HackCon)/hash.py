# I was bored and high af and thought of making a visual hash function where instead of a digest we get a png as hash of a string 
# So I developed this algorithm to hash the flag. (Patent pending, don't even think of copying it)
# It is so secure that you need more computation to break this than to break a sha256 hash

import base64
import math
import hashlib
from PIL import Image

flag = "d4rk{sample_flag123}c0de"

def encode(s):
	return (''.join([ chr(ord(c)+4) for c in s[::-1] ]))

def base64encode(s):
	return base64.b64encode(s.encode("utf8")).decode("utf8")

b64_flag = base64encode(flag)

encrypted_flag = ""
temp_str = ""

for i in b64_flag:
	temp_str += i
	encrypted_flag += encode(temp_str)

print(encrypted_flag)

pixels_list = []

checksum = 0
for i in encrypted_flag:
	m = hashlib.md5()
	m.update(i)
	m = m.hexdigest()
	m = int(m, 16)
	checksum += m
	m = str(hex(m))
	for j in range(0, len(m)-3, 3):
		pixels_list.append((128 + ord(m[j])^ord(m[j+1]), 128 + ord(m[j+1])^ord(m[j+2]), 128 + ord(m[j+2])^ord(m[j+3])))

print(checksum)
while checksum>0:
	pixels_list.append(((checksum%256), ((checksum/256)%256), ((checksum/(256*256))%256)))
	checksum = checksum/(256**3)
	
image_out = Image.new("RGB",(int(math.ceil(math.sqrt(len(pixels_list)))),int(math.ceil(math.sqrt(len(pixels_list))))))
image_out.putdata(pixels_list)
image_out.save('digest.png')
