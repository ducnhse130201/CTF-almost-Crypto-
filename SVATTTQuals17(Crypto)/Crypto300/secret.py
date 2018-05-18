import random
import os
import string
from base64 import *

FLAG="SVATTT2017{kh0n9_du0c_du_l1ch_D4_N4NG_r01_CVE_2017_9248}"


def random_str(N):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(N))

def gen_data_kv():
    n1 = random.randint(5, 20)
    n2 = random.randint(30, 100)
    k = random_str(n1)
    v = random_str(n2)
    return '"%s": "%s"' % (k,v)

def gen_data(u,f):
    return '{"a":"%s", %s, "pin": "%s", %s, "flag": "%s", %s}' %(random_str(3), gen_data_kv(), u, gen_data_kv(), f, gen_data_kv())

def pack_pin(u):
    return gen_data(u, FLAG)
