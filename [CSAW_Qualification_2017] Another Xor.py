import hashlib
cipher = '274c10121a0100495b502d551c557f0b0833585d1b27030b5228040d3753490a1c025415051525455118001911534a0052560a14594f0b1e490a010c4514411e070014615a181b02521b580305170002074b0a1a4c414d1f1d171d00151b1d0f480e491e0249010c150050115c505850434203421354424c1150430b5e094d144957080d4444254643'.decode('hex')
'''
format_flag = 'flag{'

part_key = xor(cipher[:5],format_flag)	# key[:5] = 'A qua'
md5_xor = cipher[-32:]		

#Analysis printable chars at every off set of md5 string (hex string [0-9a-f])

for i in range(len(md5_xor)):
	print 'Index %d' % i
	for j in range(33,128):
		tmp = chr(j ^ ord(md5_xor[i]))
		if tmp in '0123456789abcdef':
			print chr(j),
	print '\n'+'-----------------------------------------------'
'''	

s = 'flag{' + '_'*(38-6) + '}A qua' + '_'*(67-5)
s += hashlib.md5(s).hexdigest()
a = 'A qua' + '_'*(67-5) + 'A qua' + '_'*(67-5) + 'A q'

prev = ''
while s!= prev:
	prev = s
	prefix = s[:105]
	s = list(s)
	a = list(a)
	# change and plus md5(plaintext + key) in every loop
	md5 = list(hashlib.md5(prefix).hexdigest())
	for i in range(32):
		s[i+105] = md5[i]
	

	for i in range(len(s)):
		if s[i] == '_' and a[i] != '_':
			s[i] = chr(ord(cipher[i])^ord(a[i]))
		if s[i] != '_' and a[i] == '_':
			a[i] = chr(ord(cipher[i])^ord(s[i]))

	s = ''.join(s)
	a = ''.join(a)

	a = s[38:105]*2 + 'A q'

print 'Plaintext: ' + s		# recover: plaintext + key + md5(plaintext + key)




	
















	
