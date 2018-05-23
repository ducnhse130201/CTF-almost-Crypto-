import subprocess
from telnetlib import *
from base64 import *

host,port = 'meepwn.team', 54321

r = Telnet(host,port)
def reg(uname,passwd):
	#r = Telnet(host,port)
	a = r.read_until('>>> ')
	#print a
	r.write('1\n')
	a = r.read_until('Username: ')
	#print a
	r.write(uname+'\n')
	a = r.read_until('Password: ')
	#print a
	r.write(passwd+'\n')	
	a = r.read_until('login: ')
	cipher = r.read_until('\n').strip()
	return cipher

def login(cre):
	#r = Telnet(host,port)
	a = r.read_until('>>> ')
	#print a
	r.write('2\n')
	a = r.read_until('Enter your creds: ')
	#print a
	r.write(cre+'\n')
	r.interact()

def parse(cipher):
	cipher = b64decode(cipher)
	sign = cipher[-40:]
	data = cipher[:-46]
	return sign,data


def hash_length_ex(data,len_secret,append,sign,_format):
	res_sign = ''
	res_string = ''
	command = './hash_extender/hash_extender -d "' + data + '" -l ' + str(len_secret) + ' -a "' + append + '" -s "' + sign + '" -f "' + _format + '"'

	p = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	for line in p.stdout.readlines():		
		if line.startswith('New signature:'):
			res_sign = line.split(' ')[2].strip()
		
		if line.startswith('New string:'):
			res_string = line.split(' ')[2].strip()
	
	retval = p.wait()

	return res_sign,res_string

# run every part to find full flag


# part1
cipher = reg('admin','abc')
print 'Cres: ' + cipher
sign,data = parse(cipher)
new_sign,new_string = hash_length_ex(data,16,'&ROLE=1',sign,'sha1')
new_cre = b64encode(new_string.decode('hex') + '&sign=' + new_sign)
print 'New cres: ' + new_cre
login(new_cre)

'''
# part2
key1 = '01FE01FE01FE01FE'.decode('hex')
key2 = 'FE01FE01FE01FE01'		# input key2 when interact with server

cipher = reg('iamgroot',key1)
print 'Cres: ' + cipher
sign,data = parse(cipher)
new_sign,new_string = hash_length_ex(data,16,'&ROLE=2',sign,'sha1')
new_cre = b64encode(new_string.decode('hex') + '&sign=' + new_sign)
print 'New cres: ' + new_cre
login(new_cre)
'''











