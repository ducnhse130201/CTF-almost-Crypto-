#!/usr/bin/env python

from random import *
import SocketServer
import threading
from Crypto.Cipher import DES
from Crypto import Random
from hashlib import sha256
import os
import random
from ctf import welcome_mess,goodluck_mess
from ctf import FLAG

BS = DES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


class DESCipher:
    def __init__(self, key):
        """
        Requires hex encoded param as a key
        """
        self.key = key.decode("hex")

    def encrypt(self, raw):
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        iv = Random.new().read(BS)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        return (iv + cipher.encrypt(raw)).encode("hex")


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def get_challenge(self):
        return os.urandom(random.randint(24, 48))

    def init(self):
        self.seed = os.urandom(2).encode("hex")
        self.challenge = self.get_challenge()
        self.key = sha256(sha256(self.seed).hexdigest()).hexdigest()[:BS*2]
        des = DESCipher(self.key)
        self.cipher = des.encrypt(self.challenge).encode("hex")

    def handle(self):
        self.request.settimeout(5)
        rsend = self.request.sendall
        rclose = self.request.close
        rrecv = self.request.recv

        rsend(welcome_mess + "\n\n\n")

        self.init()
        rsend("Solve my challenge and I will fulfill your wish: " + self.cipher + "\n")
        rsend('So, what is my challenge ???\n')
        user = rrecv(2048).rstrip('\n')
        if user == sha256(self.challenge).hexdigest():
            rsend('Excellent! Here is the flag: ' + FLAG + '\n')
        else:
            rsend(goodluck_mess + '\n')

        rclose()


HOST, PORT = 'localhost', 33334
while True:
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    server_thread.join()
