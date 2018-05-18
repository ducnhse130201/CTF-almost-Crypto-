from Crypto.PublicKey import RSA
import os

flag = open('flag','r').read()
assert flag.startswith('MATESCTF') == True
welcome = """
-------------------------------------------------------------------------------
 ,  _,  _, __,  _,.  . __ .__ .   ,.__ __, ,  _, .  .  ._, _,.__ .  . ,  __  _,
/| '_) '_)  /  '_)|\ |/  `[__) \./ [__) / /| |.| |\ |  |_ '_)[__)\  //| /  `'_)
 | ._) ._) /   ._)| \|\__.|  \  |  |   /   | |_| | \|  ._)._)|  \ \/  | \__.._)
-------------------------------------------------------------------------------
"""

n = RSA.generate(1024,os.urandom).n
e = 5
bs = 16

def encrypt(s):
  s = s + chr(bs-len(s)%bs)*(bs-len(s)%bs)
  return hex(pow(int(s.encode('hex'),16),e,n))

print welcome
print 'We will give you the flag to prove how 5ecur3 our service is:'
print '-------------------------'
print 'N:\t', hex(n)
print 'Flag:\t', encrypt(flag)
print '-------------------------'
print '0nly h4x0r can see the flag'
print 'Now send me some message to encrypt:'

while True:
  m = raw_input()
  if len(m) == 0:
    break
  print 'Here you go:'
  print '-------------------------'
  print encrypt(m)
  print '-------------------------'

print 'I hope you guys have fun :)'