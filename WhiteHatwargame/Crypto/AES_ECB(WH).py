import urllib2
import urllib
from hashlib import *
import string
def getdata(str):
	url = 'http://chall04-crypto02.wargame.whitehat.vn'
	values = {}
	values['crypto'] = str.encode('base64')
	data = urllib.urlencode(values)
	req = urllib2.Request(url,data)
	res = urllib2.urlopen(req).read()
	base64 = res.split('<p>')[1].split('</p>')[0].strip()
	return base64.decode('base64').encode('hex')

alphabet = string.printable
flag = ''
for j in range(14):
	for i in alphabet:
		text = 'a'*(21-len(flag))+flag+i+'something!'+'a'*(21-len(flag))
		data = getdata(text)
		if data[:64] == data[64:64*2]:
			flag += i
			print flag
			break
	
