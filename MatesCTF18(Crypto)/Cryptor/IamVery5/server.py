#!/usr/bin/python2
import sys
import hashlib
import gmpy2
import json
from secret import q, a, b, FLAG

e = 65537
cmd = "Matesctf#crifto"

class JSONObject:
	def __init__(self, d):
		self.__dict__ = d

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)
sys.stderr = None

def H(m):
	return hashlib.sha256(m).hexdigest()

def F(x):
	return x, square_roots(pow(x, 3, q) + a * x + b, q)

def square_roots(a, m):
	if m % 4 != 3: 
		return None
	s = pow(a, (m + 1) // 4, m)
	#we just need one solution, the other solution is `m - s`
	return s

def is_valid(P):
	if P == (0, 0):
		return True
	l = P[1] ** 2 % q
	r = (P[0] ** 3 + a * P[0] + b) % q
	return l == r

def _add(a, b, q, P, Q):
	"""
	point addition, from
	https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition
	""" 
	if P == (0, 0):
		return Q[0], Q[1]
	elif Q == (0, 0):
		return P[0], P[1]
	if P != Q:
		L = (Q[1] - P[1]) * gmpy2.invert(Q[0] - P[0], q) % q
	else:
		L = (3 * P[0] ** 2 + a) * gmpy2.invert(2 * P[1], q) % q

	Rx = (L ** 2 - P[0] - Q[0]) % q
	Ry = (L * P[0] - L * Rx - P[1]) % q

	return int(Rx), int(Ry)

def _mul(a, b, q, n, P):
	"""
	point multiplication, double-and-add method from
	https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Double-and-add
	"""
	R = (0, 0)
	while n:
		if n & 1:
			R = _add(a, b, q, R, P)
		P, n = _add(a, b, q, P, P), n // 2
	return R

def verify(signature):
	try:
		S = signature.decode("base64")
		data = json.loads(S, object_hook=JSONObject)

		s = int(data.sig, 16)

		if s >= q:
			return "[Errno 400] Bad Signature"

		checkpoint = F(s)

		if checkpoint[1] == None:
			return "[Errno 40O] Bad Signature: %s" % checkpoint[0]

		h = int(H(data.msg), 16)
		if _mul(a, b, q, e, checkpoint)[0] == h:
			return data.msg
		else:
			return "[Errno 4OO] Bad Signature: (%s, %s)" % checkpoint
	except:
		return "[Errno 0x1337] Invalid"

for i in range(0x1337):
	SIGNATURE = raw_input('Your signature: ')
	result = verify(SIGNATURE)
	if cmd in result:
		print "Good job, here is your flag!"
		print FLAG
		sys.exit(0)
	else:
		print result
print "Bye!"