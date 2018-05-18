from Crypto.PublicKey import RSA

secret_message = None

key = open('key.txt','r').read().split()
for line in key:
	N,e = line[1:-1].split(',')
	cipher = RSA.construct( ( long(N),long(e) ) )
	secret_message = cipher.encrypt(secret_message,1)[0]

print hex(secret_message)
# 0xcab0130b5edf8a983ae7acc1f3b0e804c73e14aa28bc44e7766478a30f23117ddd12217b4744fafafde645d396e9884b1cb6ebe94312a3983699751776dc50fL