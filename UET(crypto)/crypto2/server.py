from Crypto.PublicKey import RSA
import os
import SocketServer
import threading

flag = "UETCTF{RSA_1s_3a5y!_tRy_4n0th3r_0n3}"
host = "localhost"
port = 33335

class incoming(SocketServer.BaseRequestHandler):
  def handle(self):
    cur_thread = threading.current_thread()
    N = RSA.generate(1024,os.urandom).n
    welcome = """
-------------------------------------------------------------------------------
 ,  _,  _, __,  _,.  . __ .__ .   ,.__ __, ,  _, .  .  ._, _,.__ .  . ,  __  _,
/| '_) '_)  /  '_)|\ |/  `[__) \./ [__) / /| |.| |\ |  |_ '_)[__)\  //| /  `'_)
 | ._) ._) /   ._)| \|\__.|  \  |  |   /   | |_| | \|  ._)._)|  \ \/  | \__.._)
-------------------------------------------------------------------------------
"""
    req = self.request
    req.send(welcome)
    
    #You can't see me, My time is now
    req.send("We will give you the flag to prove how 5ecur3 our service is:\n")
    req.send("-------------------------\n")
    req.send("N: " + str(hex(N)) + "\n")
    req.send("Flag: " + str(hex(pow(int(flag.encode("hex"), 16),5,N))) + "\n")
    req.send("-------------------------\n")
    req.send("0nly h4x0r can see the flag\n")
    
    while True:
      req.send("\nNow send me some message to encrypt:\n")
      m = req.recv(1024)
      req.send("Here you go:\n")
      req.send("-------------------------\n")
      req.send(str(hex(pow(int(m.encode("hex"), 16),5,N))) + "\n") 
      req.send("-------------------------\n")

class ReuseableServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

server = ReuseableServer((host, port), incoming)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()
server_thread.join()
