import binascii
import base64
import random

BS = 8
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def keymix(key, counter):
    r1 = 0
    r2 = 0
    r3 = 0
    key = (counter<<64) | key
    for i in range(96):
        b = key & 0x01
        key = key >> 1

        val = ((r1&0xA4000)*0x25000)&0xFFFFFFFF
        val ^= (r1<<13)&0xFFFFFFFF
        r1 = (((r1<<1)&0xFFFFFFFF) | (val>>31)) ^ b

        val = ((r2&0x120000)*0x4800)&0xFFFFFFFF
        r2 = (((r2<<1)&0xFFFFFFFF) | (val>>31)) ^ b

        val = ((r3&0x620000)*0x4600)&0xFFFFFFFF
        r3 = (((r3<<1)&0xFFFFFFFF) | (val>>31)) ^ b

    r1 = r1 & 0xFFFFF
    r2 = r2 & 0x1FFFFF
    r3 = r3 & 0x7FFFFF

    res = r1 | (r2<<20) | (r3<<41)
    return res

def rotate(state):
    r1 = state & 0xFFFFF
    r2 = (state>>20) & 0x1FFFFF
    r3 = (state>>41) & 0x7FFFFF

    count = (((r1>>8)&0x01) + ((r2>>9)&0x01) + ((r3>>10)&0x01)) >> 1

    if ((r1>>8)&0x01) == count:
            val = ((r1&0xA4000)*0x25000)&0xFFFFFFFF
            val ^= (r1<<13)&0xFFFFFFFF
            r1 = ((r1<<1)&0xFFFFFFFF) | (val>>31)

    if ((r2>>9)&0x01) == count:
        val = ((r2&0x120000)*0x4800)&0xFFFFFFFF
        r2 = ((r2<<1)&0xFFFFFFFF) | (val>>31)

    if  ((r3>>10)&0x01) == count:
        val = ((r3&0x620000)*0x4600)&0xFFFFFFFF
        r3 = ((r3<<1)&0xFFFFFFFF) | (val>>31)

    r1 = r1 & 0xFFFFF
    r2 = r2 & 0x1FFFFF
    r3 = r3 & 0x7FFFFF

    res = r1 | (r2<<20) | (r3<<41)
    return res

def encrypt(line, step, key):
    state = keymix(key, binascii.crc32(str(step)))

    for i in range(73 + step):
        state = rotate(state)
    data = pad(line)

    ks = []
    for i in range(8):
        ks.append(state>>(8*i) & 0xFF)

    for i in range(8, len(data)):
        k = 0
        for j in range(8):
            state = rotate(state)
            b = (((state>>19)^(state>>40)^(state>>63))&0x01)
            k = k * 2 + b
        ks.append(k)

    data_enc = ""
    j = 0
    for d in data:
        data_enc += chr((ord(d) ^ ks[j]) & 0xFF)
        j += 1
    return base64.b64encode(data_enc)

if __name__ == '__main__':
    key = random.getrandbits(64)
    INPUT = "file.txt"
    OUTPUT = "file.enc"
    with open(INPUT) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content.append("")

    content_enc = []
    step = 0
    for line in content:
        content_enc.append(encrypt(line, step, key))
        step += 1

    out = open(OUTPUT, "w")
    for line in content_enc:
        out.write(line + "\n")
    out.close()