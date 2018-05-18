import telnetlib
import string


def payload(s):
	s = s.encode('hex')
	p = telnetlib.Telnet('localhost','33337')
	a = p.read_until(':')
	a = p.read_until(':')
	p.write(s + '\n')
	a = p.read_until(':')
	enc = p.read_until('\n').strip()
	p.close()
	return enc.decode('hex')



flag = ''
for i in range(100):
	plain = payload('A'*(44-i))
	for char in string.printable:
		query = 'A'*(44-i)+'", "flag": "'+ flag + char
		guess = payload(query)
		if guess[:64] == plain[:64]:
			flag += char
			print flag
			break
	if flag[-1] == '}':
		break	





