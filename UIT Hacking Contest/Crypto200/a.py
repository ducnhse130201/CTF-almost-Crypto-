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

def valid(username):
    if username != "" and u'admin' not in username.lower() and not any(char not in string.printable[:62] for char in list(username)):
        return True
    return False

def generate_token(username):
    aes = AES_(key)
    cred = {}
    cred['user'] = username
    cred_encrypted = aes.encrypt(json.dumps(cred))
    return (username, cred_encrypted)

def check(token):
    aes = AES_(key)
    try:
        login = json.loads(aes.decrypt(token))
    except:
        return error
    if login['user'] == 'admin':
        return win
    else:
        return menu_user % (login['user'], login['user'])
