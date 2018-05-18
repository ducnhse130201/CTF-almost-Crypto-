cipher = '805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9'.decode('hex')
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result


format_flag = 'TWCTF{'
lst = []
for i in range(len(format_flag)):
	lst.append(ord(cipher[i]))
lst1 = []
lst2 = []

#the idea is to find a,b : ((cipher)*a + b) % 251 = plaintext

# we can find it base on format flag

#making first list
for i in range(256):
	for j in range(256):
        	num1 = (lst[0]*i+j) % 251
		if num1 == ord(format_flag[0]):
			lst2.append([i,j])

# finding common elements between lists
for c in range(2,len(format_flag)):
	for i in range(256):
		for j in range(256):
                        num1 = (lst[c]*i+j) % 251
                        if num1 == ord(format_flag[c]):
                                lst1.append([i,j])
	lst2 = common_elements(lst1,lst2)
	lst1 = []

# use a,b from final_list to decrypt :D

a,b = lst2[0][0],lst2[0][1]
print a,b
flag = ''

for i in range(len(cipher)):
	flag += chr((a*ord(cipher[i]) + b) % 251)

print flag









