# Created with Python 3.10.0
# CS4640 Homework #2 RSA cipher

import math
import sys
import random

# RC4 Stream cipher
# Order of arguments: operation input m n
def RSA(operation, input, m ,n):
    if(operation == "encrypt"):
        # Convert input to int and start key generation
        p = int(m)
        q = int(n)
        n = p * q
        phi = (p-1)*(q-1)
        e = 3
        es = []

        # Find a random e such that gcd(e, phi) = 1
        for i in range(phi):
            if(math.gcd(i,phi) == 1):
                es.append(i)
        e = random.choice(es)

        # python Modular multiplicative inverse
        d = pow(e, -1, mod=phi)

        input = int(input)

        c = (input ** e) % n

        print("Ciphertext = " + str(c)) 
        print("Private Key = " + str(d) + ", " + str(n))
        print("Public Key = " + str(e) + ", " + str(n))

    if(operation == "decrypt"):
        # compute m = c^d mod n 
        p = (int(input) ** int(m)) % int(n)   

        print("Plaintext = " + str(p))

RSA(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
