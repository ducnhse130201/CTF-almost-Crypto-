# 2018.04.27 15:01:26 +07
#Embedded file name: ./makefile.py
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
flag = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
e = 17L
p = getPrime(2048)
q = getPrime(2048)
n = p * q
m = int(flag.encode('hex'), 16)
c1 = pow(m + 525689, e, n)
f = open('ciphertext1', 'w')
f.write(hex(c1)[2:-1].decode('hex'))
f.close()
c2 = pow(m + 614039, e, n)
f = open('ciphertext2', 'w')
f.write(hex(c2)[2:-1].decode('hex'))
f.close()
rsa = RSA.construct((n, e))
f = open('pubkey', 'w')
f.write(rsa.publickey().exportKey())
f.close()
+++ okay decompyling makefile.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2018.04.27 15:01:26 +07
