import os
import socket
import threading
from hashlib import *
import SocketServer
from Crypto.Cipher import AES
import string
from base64 import *
host, port = 'localhost', 33337
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        flag = 'PTITCTF{Mami_T0day_i_l3arn_H0w_to_br3ak_AES_by_Their_Mistake}'
	hmd5 = md5(flag).hexdigest()
	obfus = len(hmd5)/3
	iv = 'hardh4rddr4hdrah'
 	key = 'w3lldon3m3nh4h4d'
	self.request.sendall("W3lc0m3 to k0m4ng S3s1on G3n3r4t0r Syst3m! \n")
	self.request.sendall("Username: ")
	user = self.request.recv(1024).strip()
	if ( len(user) > 43 ):
		self.request.sendall("No, dont hack me please \n")
		self.request.close()
	else:
	     self.request.sendall("Password: ")
	     pwd = self.request.recv(1024).strip()
	     if ( len(pwd) > 43 ):
		     self.request.sendall("No, dont hack me please \n")
		     self.request.close()
	     else:
	        session = hmd5[:obfus] + user + pwd + flag
	        while ( len(session) % 32 != 0 ):
	            session+= ' '
		obj = AES.new(key,AES.MODE_CBC,iv)
	        cipher = obj.encrypt(session)
                self.request.sendall('Your encrypted session: ' + b64encode(cipher) + '\n' )
    	        self.request.close()

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
