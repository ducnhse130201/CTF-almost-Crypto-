cipher = 'ENDTBTXNYVULWOFKJEGBYSTFPFMJFYMNVCBPYDDFSQOKEGPKX'
key =     '0011110111001101111010111010110101101011110110110'
plain = ''
rot = 0
for i in range(len(cipher)):
	rot += int(key[i])
	num = ord(cipher[i]) - rot
	if num < 65:
		num += 26
	plain += chr(num)

print plain

 
