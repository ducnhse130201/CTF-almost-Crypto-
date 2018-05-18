import httplib
import urllib
import math
def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2,int(math.sqrt(n))+1):
			if n % i == 0:
				return False
	return True


connect = httplib.HTTPConnection('hack.bckdr.in')
response = connect.request('GET', 'http://hack.bckdr.in/2013-MISC-75/misc75.php')
response = connect.getresponse()

html = response.read()
value =  int(html.split()[15])

count = 0
n = 2
sum = 0
while count <= value:
	if isPrime(n):
		sum += n
		count += 1
	n += 1
print value
print sum

headers = response.getheaders()
cookies = headers[1][1]

headers = {
        "Content-type" : "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Cookie": cookies,
        "Host": "hack.bckdr.in",
        "Referer": "http://hack.bckdr.in/2013-MISC-75/misc75.php",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }

send = urllib.urlencode({'answer': sum,'submit':'Submit'})
result = connect.request("POST","http://hack.bckdr.in/2013-MISC-75/misc75.php",send ,headers)
result = connect.getresponse()
print result.read()