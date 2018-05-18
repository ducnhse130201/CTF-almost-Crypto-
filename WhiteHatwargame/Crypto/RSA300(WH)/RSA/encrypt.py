from Crypto.Util import number

from secret import M, flag

p = number.getPrime(512)
q = number.getPrime(512)
n = p * q
e = 3

assert (len(flag) < 18),"Fail!"

fsplit = len(flag)/3

m1 = M + chr(number.getRandomRange(32, 128)) + flag[:fsplit]
m2 = M + chr(number.getRandomRange(32, 128)) +  flag[fsplit:2*fsplit]
m3 = M + chr(number.getRandomRange(32, 128)) +  flag[2*fsplit:]

m1 = int(m1.encode('hex'),16)
m2 = int(m2.encode('hex'),16)
m3 = int(m3.encode('hex'),16)

C1 = pow(m1, e, n)
C2 = pow(m2, e, n)
C3 = pow(m3, e, n)
