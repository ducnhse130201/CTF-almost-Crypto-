import ContinuedFractions, Arithmetic
import sys
from binascii import *
n = int(sys.argv[1])
e = int(sys.argv[2])
c = int(sys.argv[3])


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    print(" e = " );
    print (e)
    print(" n = " );
    print(n)
    print("d = ")
    print(hack_RSA(e, n))    
    print("m =")
    m = pow ( c , hack_RSA(e, n) , n )
    print unhexlify(format(m,'x'))
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    test_hack_RSA()
