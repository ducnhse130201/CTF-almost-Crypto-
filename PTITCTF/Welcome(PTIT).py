cipher = 'KGRGXGU{Xszl_nfmt_wvm_elr_xflx_gsr_XGU_KGRG}'

flag = ''

for i in range(len(cipher)):
	if cipher[i].isalpha():
		if cipher[i].isupper():
			flag += chr(-ord(cipher[i]) + (65+90))
		if cipher[i].islower():
			flag += chr(-ord(cipher[i]) + (97+122))
	else:
		flag += cipher[i]
#atbash cipher(special case of affine cipher)
print flag
