
#find two close primes
from math import ceil
import sys
def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b

    print "p = ",p
    print "q = ",q
    return p, q

from libnum import *
to_int = lambda string : int(string,16)
n = 1552518092300708935148979488462502555256886017116696611139052038026050952686376886330878408828646477971459063658923221258297866648143023058142446317581796810373905913084934869211153276980011573717416472395713363686571638755823503877
BS = 32
p,q = fermat(n)
phi = (p-1)*(q-1)
e = 3
d = modular.invmod(e,phi)
f = open('cipher.txt').read()

lst_c = f.split(' ')
c0 = to_int(lst_c[0])
print n2s(pow(c0,d,n))

for i in range(1,len(lst_c)):
	c = pow(to_int(lst_c[i]),d,n)
	c1 = int(hex(to_int(lst_c[i-1]))[2:-1][:BS*2+1], 16)
	m = c - c1
	print n2s(m)
	















