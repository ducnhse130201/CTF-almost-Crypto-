# 2018.04.23 19:41:36 +07
#Embedded file name: /root/Desktop/ctf-2017/rade/makefile.py
from FLAG import *
from Crypto.Util.number import *
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e1 = 17
e2 = 23
m1 = pow(flag, e1, n)
m2 = pow(flag, e2, n)
c1 = pow(m1 + 12345, e1, n)
c2 = pow(m1 + 56789, e1, n)
c3 = pow(m2 + 12345, e2, n)
c4 = pow(m2 + 56789, e2, n)
+++ okay decompyling makefile.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2018.04.23 19:41:37 +07
