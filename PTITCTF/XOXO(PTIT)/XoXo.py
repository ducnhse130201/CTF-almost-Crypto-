def xor(s1, s2):
    res = [chr(0)]*8
    for i in range(len(res)):
        k = ord(s1[i]) ^ ord(s2[i])
        res[i] = chr(k)
    res = ''.join(res)
    return res

def add_pad(msg):
    l = 8 - len(msg) % 8
    msg += chr(l)*l
    return msg

with open('flag.png', 'rb') as f:
    data = f.read()

data = add_pad(data)

with open('key') as f:
    key = f.read()

enc_data = ''
for i in range(0, len(data), 8):
    enc = xor(data[i:i+8], key)
    enc_data += enc

with open('flag_enc.png', 'wb') as f:
    f.write(enc_data)


