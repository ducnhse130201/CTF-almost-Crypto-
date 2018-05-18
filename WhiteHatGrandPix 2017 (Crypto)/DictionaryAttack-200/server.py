import enchant
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import threading
import urlparse
import os
import re
from Crypto.Cipher import DES3

html="""<html>
    <head>
        <title>
        Welcome to the ultimate crypto stage!
        </title>
    </head>
        <h1>1975: Road to Saigon</h1>
        <img src="https://i.pinimg.com/736x/04/bd/c0/04bdc0186c09d1b43524bdb902b5a8b9--vietnam-war-vietnam-history.jpg"> </img>
        <p>People often assume that just because something is "encrypted", therefore it must be "safe".</p>
        <p>To illustrate the dangers this blind faith in cryptography, we have designed a challenge for you.</p>
        <p>In 1975, we - brothers from Hanoi - sent to our commies in the South a message via CIA satellite channel without being caught by the NSA.

        <p>Because the Americano rules are so much lame:</p>
        <ul>
            <li>We don't need to know their encryption key</li>
            <li>The plaintext we want to send was: "evil minds captured flags"</li>
            <li>Our secret spies already leaked the <a href='./server.py'>lame CIA crypto algo for us</a>.</li>
            <li>BUT, the plaintext must consist of only valid Americano words :(</li>
            <li>AND, of course we never want these following words be appeared in any CIA rules otherwise they will find out the internal spy:
                <ul>
                    <li>"evil"</li>
                    <li>"minds"</li>
                    <li>"captured"</li>
                    <li>"flags"</li>
                </ul>
            </li>
        </ul>
        <p> Good luck! </p>
        <form>
            <p>Enter your plaintext:</p>
            <input type="text" name="plaintext"><br>
            <input type="submit" value="Encrypt!">
            <p>{}</p>
            <p>Think you have found a solution? Try it!</p>
            <p>Enter your ciphertext:</p>
            <input type="text" name="ciphertext">
            <input type="submit" name="Decrypt!">
        </form>
    </body>
    </html>

"""

dictionary = enchant.Dict("en_US")

encryption_key = ""
flag = ""


def check_and_encrypt(plaintext):
    if check(plaintext):
        return encrypt(plaintext)
    return "<strong>Sorry!</strong>"

def check(plaintext):
    plaintext = re.sub(r'\s\s*', ' ', plaintext).strip().lower()
    words = plaintext.split(' ')
    evil_words = ["evil", "minds", "captured", "flags"]
    return all([dictionary.check(word) and not word in evil_words for word in words])

def encrypt(plaintext):
    crypter = DES3.new(encryption_key, DES3.MODE_ECB)
    #do some pkcs7 padding
    blocksize = 8 #crypter.block_size
    pad = blocksize - (len(plaintext) % blocksize)
    plaintext = plaintext + (chr(pad) * pad)
    ciphertext = crypter.encrypt(plaintext)
    return "Your ciphertext: " + ciphertext.encode('base64')

def decrypt(ciphertext):
    crypter = DES3.new(encryption_key, DES3.MODE_ECB)
    try:
        ciphertext = ciphertext.decode('base64')
        plaintext = crypter.decrypt(ciphertext)
        pad = ord(plaintext[-1])
        plaintext = plaintext[:-pad]
        return plaintext
    except Exception as e:
        print e
        return ""


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/server.py":
            with open("server.py") as f:
                self.wfile.write(f.read())
        else:
            message = ""
            params = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            if 'ciphertext' in params and params['ciphertext']:
                ciphertext = params['ciphertext'][0]
                plaintext = decrypt(ciphertext)
                if plaintext == "evil minds captured flags":
                    message = flag
                else:
                    message = "<strong>Sorry!</strong>"
            elif 'plaintext' in params and params['plaintext']:
                plaintext = params['plaintext'][0]
                message = check_and_encrypt(plaintext)
            self.wfile.write(html.format(message))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == "__main__":
    try:
        with open("key", "rb") as f:
            encryption_key = f.read()
        with open("flag.txt", "rb") as f:
            flag = f.read()

        server = ThreadedHTTPServer(('localhost', 33339), MyHandler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()
