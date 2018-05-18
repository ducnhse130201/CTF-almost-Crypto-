from libnum import *

f1 = open('key1').read()
lst = f1.split('\n')

n1 = int(lst[0])
e = long(lst[1])
p = int(lst[2])
q = int(lst[3])

n2 = (p+2)*(q+2)
d1 = modular.invmod(e, (p-1)*(q-1))
d2 = modular.invmod(e, (p+1)*(q+1))

c2 = int(open('encrypted').read())

c1 = pow(c2,d2,n2)

m = pow(c1,d1,n1)

print n2s(m)













