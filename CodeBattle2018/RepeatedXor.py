ciphertext = '305c0717711507470f174837010700196c2c43413c415d17014a13066c07436c3c174909'.decode('hex')
format_flag = "CodeBattle{"
flag = ''
def sxor(s1,s2):    
	b1 = bytearray(s1)
	b2 = bytearray(s2)
	b = bytearray(len(s1))
	for i in range(len(s1)):
		b[i] = b1[i] ^ b2[i]
	return b
def repeat(string, len_cipher):
    return (string*(int(len_cipher/len(string))+1))[:len_cipher]

#making len(key) == len(ciphertext)
#-----------------------------------------------------------------------#

#print sxor(ciphertext[:11],format_flag)
# A ^ B = C => C ^ B = A(format_flag ^ ciphertext[:11] => key[:11])	=> output: s3cr3ts3cr3 => reapeated Xor with key: s3cr3t

key = repeat('s3cr3t',len(ciphertext))
print key
print sxor(ciphertext,key)
