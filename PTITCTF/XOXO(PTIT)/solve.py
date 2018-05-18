def xor(s1, s2):
    res = [chr(0)]*8
    for i in range(len(res)):
        k = ord(s1[i]) ^ ord(s2[i])
        res[i] = chr(k)
    res = ''.join(res)
    return res


with open('XoXo(PTIT).png','rb') as f:
	enc_data = f.read()

text = enc_data[:8]
png_header = '89504e470d0a1a0a'.decode('hex')
key = ''
for i in range(8):
	key += chr(ord(text[i]) ^ ord(png_header[i]))

data = ''

for i in range(0,len(enc_data),8):
	data += xor(enc_data[i:i+8],key)
with open('flag.png','wb') as f:
	f.write(data)
	


