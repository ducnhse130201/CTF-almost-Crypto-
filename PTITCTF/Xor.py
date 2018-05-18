encrypted_flag = "7074497447744a9f736f619963746861942b9763659293956b68636b9393646c95676f636b9599979d".decode("hex")
grep = "PTITCTF{"
toGrep = ""
#loop to find hidden pad
string = encrypted_flag[:8]
for pad in range(1,21): # cause pad from the code is random from 0,20.So i starta loop to find it
        for char in string:
                num_a = ord(char)
                num = (num_a ^ pad) - pad
                char = chr(num)
                toGrep += char
        if toGrep == grep:
                print 'Here your pad. Use it and have fun:' + str(pad)
                break
        else:
                toGrep = ""


#after find the pad. Continue decrypt and have the flag
flag = ""
for char in encrypted_flag:
        num_a = ord(char)
        num = (num_a ^ pad) - pad
        char = chr(num)
        flag += char
print flag

