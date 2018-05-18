import string
cipher_text = "CCctNXFgdEoiPwYLAVtrW2QzOwYaPnEEFW4iISwJDlsTHB9CdiwXAFZJ".decode('base64')
grep = "PTITCTF{" + "N"
flag = ""
key = ""
index = 0
for i in range(9):
	num = ord(cipher_text[i])
	for B in range(0,255):
		index = index % 9
		char_flag = chr(num ^ B)
		if char_flag == grep[index]:
			key += chr(B)
			break
	index = index + 1

index = 0
for i in range(len(cipher_text)):
        index = index % 9
        num = ord(cipher_text[i])
        char_flag = chr(num ^ ord(key[index]))
        flag += char_flag
        index = index + 1
print 'Key: %s\n' %key
print 'Flag: %s\n' %flag
		
		

		
		
		
