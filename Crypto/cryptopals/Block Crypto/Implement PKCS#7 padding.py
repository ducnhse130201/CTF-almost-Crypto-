from Crypto.Cipher import AES
from random import randint
def xor(a,b):
	c = bytearray(len(a))
	for i in range(len(a)):
		c[i] = a[i] ^ b[i]
	return c

def pad_pkcs7(buffer, block_size):
	if len(buffer) % block_size:
		padding = (len(buffer) / block_size +1) * block_size - len(buffer)
	else:
		padding = 0

	assert 0 <= padding <= 255

	new_buffer = bytearray()
	new_buffer[:] = buffer
	new_buffer += bytearray([chr(padding)]*padding)
	return new_buffer

def unpad_pkcs7(buffer):
	#check if end byte is padding or not. If end byte is not padding then return buffer
	padding = buffer[-1]
	for i in range(len(buffer)-1,len(buffer)-padding-1,-1):
		if buffer[i] != padding:
			return buffer
	#else return buffer by
	new_buffer = bytearray()
	new_buffer[:] = buffer[:-padding]
	return new_buffer

def aes_128_ecb_enc(buffer, key):
    obj = AES.new(key, AES.MODE_ECB)
    return bytearray(obj.encrypt(bytes(buffer)))

def aes_128_ecb_dec(buffer, key):
    obj = AES.new(key, AES.MODE_ECB)
    return bytearray(obj.decrypt(bytes(buffer)))

def aes_128_cbc_enc(buffer,key,iv):
	plaintext = pad_pkcs7(buffer, AES.block_size)
	ciphertext = bytearray(len(plaintext))
	prev_block = iv
	for i in range(0,len(plaintext),AES.block_size):
		ciphertext[i:i+AES.block_size] = aes_128_ecb_enc((xor(plaintext[i:i+AES.block_size],prev_block)), key)
		prev_block = ciphertext[i:i+AES.block_size]
	return ciphertext

def aes_128_cbc_dec(ciphertext, key, iv):
    plaintext = bytearray(len(ciphertext))
    prev_block = iv
    for i in range(0, len(ciphertext), AES.block_size):
        plaintext[i: i + AES.block_size] = xor(
            aes_128_ecb_dec(bytes(ciphertext[i: i + AES.block_size]), key),
            prev_block
        )
        prev_block = ciphertext[i: i + AES.block_size]
    return unpad_pkcs7(plaintext)

def random_key(length):
    key = bytearray(length)
    for i in range(length):
        key[i] = chr(randint(0, 255))
    return key

key = bytes(random_key(16))

def encryption_oracle(data):
    unknown_string = bytearray((
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\n" +
        "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\n" +
        "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\n" +
        "YnkK"
    ).decode("base64"))
    plaintext = pad_pkcs7(
        data + unknown_string,
        AES.block_size,
    )
    return aes_128_ecb_enc(plaintext, key)


def get_block_size(oracle):
    ciphertext_length = len(oracle)
    oracle = bytearray(oracle)
    i = 1
    while True:
        data = bytearray("A" * i)
        oracle.extend(data)
        new_ciphertext_length = len(oracle)
        block_size = new_ciphertext_length - ciphertext_length
        if block_size:
            return block_size
        i += 1
data = 'nguyenhuuduc17199@gmail.com'
oracle = encryption_oracle(data)

print get_block_size(oracle)


