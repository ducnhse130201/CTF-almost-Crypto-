import base64
import string
import json
from secret import pack_pin
import SocketServer
import threading

def read_key():
    key = open("KEY.txt").read()
    key = key.decode('hex')
    return key

def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))

def encode(data):
    try:
        return base64.b64encode(data)
    except:
        return "Incorrect"

def decode(data):
    try:
        return base64.b64decode(data)
    except:
        return "Incorrect"

def unpack_pin(data):
    try:
        dt = json.loads(data)
        if 'pin' in dt:
            return dt['pin']
    except:
        pass
    return "None"

def gen_cookie(p, k):
    data = pack_pin(p)
    return encode(xor(bytearray(encode(data)), bytearray(k)))

def load_cookie(c, k):
    data = decode(c)
    if data == "Incorrect":
        return data
    data = xor(bytearray(data), bytearray(k))
    data = decode(data)
    if data == "Incorrect":
        return data
    return unpack_pin(data)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def init(self):
        pass

    def handle(self):
        self.request.settimeout(30)
        rsend = self.request.sendall
        rclose = self.request.close
        rrecv = self.request.recv
        key = read_key()
        if len(key) != 64:
            rsend("Invalid key!\n")
            rclose()

        rsend("Welcome to secret service.\n\n")
        rsend("Please choose:\n")
        rsend("1: Cookie generator\n")
        rsend("2: Cookie verification\n")
        rsend("=======================================\n\n")
        while True:
            rsend("Choose your number[1,2]:\n")
            choose = rrecv(4096).rstrip('\n').rstrip('\r')
            if (choose == "1"):
                rsend("Please enter your pin:\n")
                pin = rrecv(4096).rstrip('\n').rstrip('\r')

                if len(pin) >= 4:
                    pin = pin[:4]

                cookie = gen_cookie(pin, key)
                rsend("Your cookie: " + cookie + "\n")
                rsend("--------------------\n")
            elif (choose == "2"):
                rsend("Please enter your cookie:\n")
                cookie = rrecv(4096).rstrip('\n').rstrip('\r')
                pin = load_cookie(cookie, key)
                rsend("Your pin: " + pin + "\n")
                rsend("--------------------\n")
            else:
                rsend("Only 1 or 2. Bye\n")
                break

        rclose()


HOST, PORT = 'localhost', 33333
while True:
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    server_thread.join()
