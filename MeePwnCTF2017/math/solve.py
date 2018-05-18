import string
import itertools
from numpy import *
from hashlib import *
from Crypto.Util.number import *
hack = 64364485357060434848865708402537097493512746702748009007197338675

factors = [3,3,5,5,7,107,487,607,28429,29287,420577267963,3680317203978923,1002528655290265069]
#fuzzing and found len(pad) == 39

def func(prd,n):
	m = prd / n
	if m*n == prd:
		return True
	return False

def check(num):
	if len(str(num)) == 39:
		return True
	return False

comb = list(itertools.permutations(factors,6))
# finding lst_pad

lst_pad = []


for i in comb:
	p = 1
	for j in range(6):
		p *= i[j]
		if p not in lst_pad and check(p):
			lst_pad.append(p)

lst = []
# recursion func to reveal all possible flag
def re(x,d):
	temp = d
	for i in range(48,128):
		if x % i == 0:	
			temp = chr(i) + d
			if len(temp) == 14 and x == i:
				lst.append(temp)
			re(x/i-1,temp)
	

for i in range(len(lst_pad)):
	a = hack / lst_pad[i]
	re(a,'')
	
# checking and print the flag
for i in lst:
	for j in range(len(lst_pad)):
		if bytes_to_long(md5(i).digest()) == lst_pad[j]:
			print 'Found!!! Flag is: ' + 'MeePwnCTF{' + i + '}'





