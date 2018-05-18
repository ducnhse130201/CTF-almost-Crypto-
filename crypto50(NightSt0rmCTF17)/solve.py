# using xortool to calculate len(key)
cipher = '250c1e2812634454105c4b01573407003403436f3b3d4900623b34094a74026f6f3b16016f440c583a26365542493b3d6e6f6f3b075549705600005452015e573b343a261f39565c50056e6f6f3b5f11261f39004857530203035758564a73517006065507060519'.decode('hex')
flag_format = 'NightSt0rm{'
def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))
# find key[:11]
def repeat(string, len_cipher):
    return (string*(int(len_cipher/len(string))+1))[:len_cipher]

a = XOR(cipher[:11],flag_format)
key = a + '0' + 'd'
print key	
alpha = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@_'
key = repeat(key,len(cipher))
print XOR(cipher,key)



