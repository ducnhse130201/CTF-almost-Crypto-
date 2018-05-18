import sys
from libnum import *
file = sys.argv[1]
with open(file,'rb') as f:
	enc = f.read()
c = s2n(enc)
print c
