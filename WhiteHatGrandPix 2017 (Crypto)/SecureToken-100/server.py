import socket
import time
import threading
import SocketServer
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
from secret import flag, seed
host, port = 'localhost', 33337

iv = hashlib.md5(seed).digest()
key = hashlib.md5(flag).hexdigest()

def block(s):
 	return [s[x:x+AES.block_size] for x in range(0, len(s), AES.block_size)]
query = '{{\"a\": \"{}\", \"flag\": \"{}\"}}'

def create_query(s):
	return query.format(s,flag)

def pad(s):
	pad_len = 16 - len(s)%AES.block_size
	return s+chr(pad_len)*pad_len

def encrypt(msg):
	# print msg
	aes = AES.new(key, AES.MODE_CBC, iv)
	return aes.encrypt(pad(msg))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		while True:
			self.request.sendall("Give me a string and i'll search it for you:\n")
			self.request.sendall("Hex string:\n")
			msg = self.request.recv(1024).strip()
			msg = msg.decode('hex')
			msg = create_query(msg)
			cipher = encrypt(msg).encode('hex')
			self.request.sendall("Your query: "+ cipher+ '\n')
			self.request.sendall("Continue? \n")
			con = self.request.recv(1024)
			if con.strip().lower() != "y":
				self.request.sendall("Bye+\n")
				self.request.close()
				break
			# pass
		
while True:
	server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
	# Start a thread with the server -- that thread will then start one
	# more thread for each request
	server_thread = threading.Thread(target=server.serve_forever)
	# Exit the server thread when the main thread terminates
	server_thread.daemon = True
	server_thread.start()
	print "Server loop running in thread:", server_thread.name
	server_thread.join()
