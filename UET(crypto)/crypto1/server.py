# _author_ = "qd"
from Crypto.Cipher import AES
from hashlib import md5
import os
import json
import SocketServer
import threading

host = 'localhost'
port = 33336
welcome = """
----------------------------------
Welcome to the S3CR3T shop
----------------------------------
Here are some options:
[R]egister
[L]ogin
[E]xit
Your choice?
"""
flag = 'UETCTF{fl11p1nG_1s_h0w_1_g0t_h3r3}'
key = os.urandom(16)

class AES_(object):
    def __init__(self, key):
        self.blocksize = 16
        self.key = md5(key.encode("hex")).digest()

    def pad(self, st):
        return st + (self.blocksize - len(st) % self.blocksize) * chr(self.blocksize - len(st) % self.blocksize)

    def unpad(self, st):
        return st[:-ord(st[len(st)-1:])]

    def encrypt(self, msg):
        msg = self.pad(msg)
        iv = os.urandom(16)
        crypt = AES.new(self.key, AES.MODE_CBC, iv)
        return (iv + crypt.encrypt(msg)).encode("base64")

    def decrypt(self, msg):
        msg = msg.decode("base64")
        iv = msg[:self.blocksize]
        crypt = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(crypt.decrypt(msg[self.blocksize:]))

class incoming(SocketServer.BaseRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        req = self.request
        while True:
            req.send(welcome)
            choice = req.recv(1024).rstrip('\n').lower()
            print choice
            if choice == 'r':
                aes = AES_(key)
                req.send('Who dares to bring an axe into my sacred groves\nShow me your name: ')
                name = req.recv(1024).rstrip('\n')
                if 'admin' in name.lower():
                    req.send('You can\'t see the forest\n')
                    continue
                else:
                    cred = {}
                    cred['user'] = name
                    cred_encrypted = aes.encrypt(json.dumps(cred))
                    req.send('The glens are calling, {0}.\nNow you can login with your credential: {1}\n'.format(cred['user'], cred_encrypted))
            elif choice == 'l':
                aes = AES_(key)
                req.send('Who are you?:\n')
                token = req.recv(1024).rstrip('\n')
                try:
                    login = json.loads(aes.decrypt(token))
                except:
                    print "Invalid credential!\n"
                    continue
                if login['user'] == 'admin':
                    req.send('Welcome back, Goddess of the Woods!\n')
                    req.send('Here\'s your flag: ' + flag)
                    req.close()
                    break
                else:
                    req.send('The glens are calling, {0}.\nBut you need to be \'admin\' to get flag!\n'.format(login['user']))
            else:
                req.send('I will rise next season.!\n')
                req.close()
                break

class ReuseableServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

server = ReuseableServer((host, port), incoming)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()
server_thread.join()
