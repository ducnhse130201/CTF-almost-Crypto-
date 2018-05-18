from telnetlib import *
from random import randint
from libnum import *
from fractions import gcd
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

m1 = 0
m2 = 10**121
m3 = 1

# creating list of rh
# let m small to do it easy
lst = []
for i in range(5):
	r = Telnet('localhost', 40001)
	r.read_until('Your choice: ')
	r.write('1')

	r.read_until('Message: ')
	r.write(n2s(m1))
	r.read_until('Ciphertext: ')
	c1 = int(r.read_until('\n'))

	r.read_until('Message: ')
	r.write(n2s(m3))
	r.read_until('Ciphertext: ')
	c3 = int(r.read_until('\n'))

	r.close()

	rh1 = c1 - m1
	rh3 = c3 - m3
	
	lst.append(rh1)
	lst.append(rh3)	

# calculate h base on gcd of many rh
res = lst[0]
for c in lst[1::]:
	res = gcd(res,c)
h = res
print 'h: ', h

#finding p
while True:
	r = Telnet('localhost', 40001)
	r.read_until('Your choice: ')
	r.write('1')
	
	r.read_until('Message: ')
	r.write(n2s(m1))
	r.read_until('Ciphertext: ')
	c1 = int(r.read_until('\n'))

	r.read_until('Message: ')
	r.write(n2s(m2))
	r.read_until('Ciphertext: ')
	c2 = int(r.read_until('\n'))	
	
	r.close()
	
	if c2 > c1:
		p = c1 + m2 - m1 - c2
		print 'p: ' ,p
		break
		
# request to find m and sendback to server to get flag
def find_m(c):
        m = c % p
        while m < 10**10 or m > 10**12:
                m = (m+p) %h
        return m

r = Telnet('localhost', 40001)
r.read_until('Your choice: ')
r.write('2')
r.read_until('Ciphertext: ')
c = int(r.read_until('\n'))

m = find_m(c)

print('Recovered m: %d' % m)
# send solution, get flag
r.write(str(m))

flag = str(r.read_until('\n'))
r.close()
print 'FLAG: ' + flag













