import struct
def decrypt(block):
	num = block >> 16
	x = num ^ block
	return x

cipher = 'CjBPewYGc2gdD3RpMRNfdDcQX3UGGmhpBxZhYhFlfQA='.decode('base64')

blocks = struct.unpack('I'*(len(cipher)/4),cipher)
out = []
for block in blocks:
	out += [decrypt(block)]

flag = ''
for block in out:
	flag += struct.pack('I',block)
print flag
