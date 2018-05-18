from sage.all import *
from Crypto.Util.number import *

#------------------------------------------------------------------------------------------------------------

#coppersmiths_short_pad_attack
def short_pad_attack(c1, c2, e, n):
    print '------------------------Starting Coppersmiths short pad attack ...---------------------------'
    PRxy.<x,y> = PolynomialRing(Zmod(n))
    PRx.<xn> = PolynomialRing(Zmod(n))
    PRZZ.<xz,yz> = PolynomialRing(Zmod(n))

    g1 = x ^ e - c1
    g2 = (x+y)^e - c2

    q1 = g1.change_ring(PRZZ)
    q2 = g2.change_ring(PRZZ)

    h = q2.resultant(q1)
    h = h.univariate_polynomial()
    h = h.change_ring(PRx).subs(y=xn)
    h = h.monic()

    kbits = n.nbits()//(2*e*e)
    diff = h.small_roots(X=2^kbits, beta=0.5)[0]  # find root < 2^kbits with factor >= n^0.5
    print 'Found diff: '
    print diff

#------------------------------------------------------------------------------------------------------------

#Stereotyped Messages (Coppersmith Attack)
def stereotyped(n,e,c,stereotyped_msg):
    print '------------------Starting Stereotyped Messages (Coppersmith Attack) ...------------------------'
    msg = msg.replace('X', '\x00')
    msg = bytes_to_long(msg)
    P.<x> = PolynomialRing(Zmod(n))
    f = (msg + x)^e - c
    f = f.monic()
    for i in range(20):
        try:    
            m = f.small_roots(epsilon=1/i)
            print 'Taking small roots with epsilon: %d' % i 
            print long_to_bytes(m[0])
            break
        except:
            i += 1
    
#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------

#Franklin-Reiter Related Message Attack
def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a.monic()

def franklinreiter(c1, c2, e, n, diff):
    print '--------------------Starting Franklin Franklin related message attack ...------------------------'
    P.<x> = Zmod(n)[]
    g1 = (x + diff)^e - c1
    g2 = x^e - c2
    print "Result"
    result = -gcd(g1, g2).coefficients()[0]
    print 'Found plaintext: '
    print long_to_bytes(result)

#------------------------------------------------------------------------------------------------------------

#Common Modulus attack
def common_modulus_attack(c1,c2,e1,e2,n):
    print '-----------------------------------Starting Common modulus attack ...----------------------------'
    g,a,b = xgcd(e1,e2)
    c1 = pow(c1,a,n)
    c2 = pow(c2,b,n)
    m = int(c1*c2)
    m = pow(m,1/g)
    print 'Found plaintext: '
    print long_to_bytes(m)
	
#------------------------------------------------------------------------------------------------------------

# Wiener Attack
def recover(e,n):
    cf = convergents(e/n)
    G.<x> = ZZ['x']
    for index, k in enumerate(cf[1:]):
        d0 = k.denominator()
        k = k.numerator()
        if k != 0 and (e * d0 - 1) % k == 0:
            
            phi = (e*d0 - 1) //k
            s = (n-phi+1)
            f = x^2 - s*x + n
            b = f.discriminant()
            if b > 0 and b.is_square():
                d = d0
                
                roots = zip(*f.roots())[0]
                if len(roots) == 2 and prod(roots) == n:
                    print("[x] Recovered! \nd = %0x" %d)
                    return d
            else:
                continue
    print("[] Could not determine the value of d with the parameters given. Make sure that d < 1/3 * n ^ 0.25")
    return -1
    

def wiener(c,e,n):
    print '-------------------------------Starting Wiener Attack ...---------------------------------------'
    d = recover(e,n)
    print 'Found plaintext: '
    print long_to_bytes(Integer(pow(c,d,n)))


#------------------------------------------------------------------------------------------------------------

#Hastad Broadcast attack
def hastad(lst_c,lst_n,e):
    print '------------------------------Starting Hastad Broadcast attack ...-------------------------------'
    M = crt(lst_c,lst_n)
    m = pow(M,1/e)
    print 'Found plaintext: '
    print long_to_bytes(m)    

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Specail Factorisation------------------------------------------

# Fermat Factorisation
def fermat(n,e,c):
    print '-------------------------------Starting Fermat factorisation ...--------------------------------'
    a = ceil(sqrt(n))
    b2 = a^2 - n
    while not is_square(b2):
        a += 1
        b2 = a^2 - n
    print 'Factoring successful'
    p = a-sqrt(b2)
    q = a+sqrt(b2)
    print 'p: ' , p
    print 'q: ' , q     
    
    phi = (p-1)*(q-1)
    d = inverse_mod(e,phi)
    m = pow(c,d,n)
    print 'Found plaintext: '
    print long_to_bytes(m)

#------------------------------------------------------------------------------------------------------------

#factoring N by Mersenne Prime (2^k - 1)
def mersenne(n,e,c):
    print '-----------------------Starting Mersenne factorisation ...-----------------------------'
    a = 4
    while True:
        if a > n:
            break
        if n % (a - 1) == 0:
            print 'Found!!'
            p = n / (a-1)
            q = a-1
            print 'p: ' , p
            print 'q: ' , q
            break
        a = a * 2
    phi = (p-1)*(q-1)
    d = inverse_mod(e,phi)
    m = pow(c,d,n)
    print 'Found plaintext: '
    print long_to_bytes(m)

#------------------------------------------------------------------------------------------------------------







