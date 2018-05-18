def decrypt_RSA(privkey, message):
    from Crypto.PublicKey import RSA 
    from Crypto.Cipher import PKCS1_OAEP 
    from base64 import b64decode 
    key = open(privkey, "r").read() 
    rsakey = RSA.importKey(key) 
    rsakey = PKCS1_OAEP.new(rsakey) 
    decrypted = rsakey.decrypt(b64decode(message)) 
    return decrypted
 
flag = "CQGd9sC/h9lnLpua50/071knSsP4N8WdmRsjoNIdfclrBhMjp7NoM5xy2SlNLLC2yh7wbRw08nwjo6UF4tmGKKfcjPcb4l4bFa5uvyMY1nJBvmqQylDbiCnsODjhpB1BJfdpU1LUKtwsCxbc7fPL/zzUdWgO+of/R9WmM+QOBPagTANbJo0mpDYxvNKRjvac9Bw4CQTTh87moqsNRSE/Ik5tV2pkFRZfQxAZWuVePsHp0RXVitHwvKzwmN9vMqGm57Wb2Sto64db4gLJDh9GROQN+EQh3yLoSS8NNtBrZCDddzfKHa8wv6zN/5znvBstsDBkGyi88NzQxw9kOGjCWtwpRw=="
print decrypt_RSA('key.priv', flag)

#if decryption by openssl not work maybe there's PLCS1_OAEP padding method. Try this decrypt function 
