from hashlib import *
f = open('hash.txt').read().strip()
f = f.split('\n')

lst = []
lst1 = []

for i in range(256):
	h = md5(chr(i)).hexdigest()
	lst.append(h)
for i in range(256):
	lst1.append(i)

dic = dict(zip(lst,lst1))

flag = ''

for i in range(len(f)):
	flag += chr(dic[f[i]])	
print flag
