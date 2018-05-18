import telnetlib
from hashlib import *
from Crypto.Cipher import DES

host = 'localhost'
port = 33334

unpad = lambda s : s[0:-ord(s[-1])]

BS = DES.block_size

def decrypt(enc,key):
	key = key.decode('hex')
	enc = enc.decode('hex')
	iv = enc[:BS]
	enc = enc[BS:]
	#print 'IV: ', iv
	#print 'Cipher: ',enc
	cipher = DES.new(key, DES.MODE_CBC,iv)
	return cipher.decrypt(enc)

keys = []
for seed in range(0x10000):
	seed = "%4x" % seed
	key = sha256(sha256(seed).hexdigest()).hexdigest()[:BS*2]
	keys.append(key)	

grep = '\x08'*8

while True:
	p = telnetlib.Telnet(host,port)
	a = p.read_until(':')
	b = p.read_until('\n').strip().decode('hex')
	if len(b) == 128:
		enc = b
		print 'Found suitable cipher: ', b.encode('hex')
		for key in keys:
			m = decrypt(enc,key)
			last = m[-8:]
			if last == grep:
				print 'Found Key: ', key
				break

		send = unpad(decrypt(enc,key))
		send = sha256(send).hexdigest()
		c = p.read_until('\n')
		p.write(send + '\n')
		print p.read_until('\n')
		break	




