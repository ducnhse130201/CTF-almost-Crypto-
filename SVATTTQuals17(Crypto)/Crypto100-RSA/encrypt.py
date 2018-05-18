import gmpy2
from ctf import MESSAGES

N = 1552518092300708935148979488462502555256886017116696611139052038026050952686376886330878408828646477971459063658923221258297866648143023058142446317581796810373905913084934869211153276980011573717416472395713363686571638755823503877
e = 3
BS = 32

to_int = lambda text: int(''.join(x.encode('hex') for x in text), 16)

c = 0L
cipher = []
for chunk in [MESSAGES[i:i + BS] for i in range(0, len(MESSAGES), BS)]:
    c1 = int(hex(c)[2:-1][:BS*2+1], 16)
    c = gmpy2.powmod(c1 + to_int(chunk), e, N)
    cipher.append(hex(c)[2:])

with open('cipher.txt', 'w') as f:
    f.write(' '.join(cipher))