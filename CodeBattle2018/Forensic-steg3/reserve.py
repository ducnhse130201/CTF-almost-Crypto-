f = open('elf','rb')
f = f.read(8701)
q = open('new_elf','wb')
q.write(f[::-1])
q.close()


