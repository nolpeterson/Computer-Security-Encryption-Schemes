# Created with Python 3.10.0
# CS4640 Homework #2 RC4 cipher

import sys

# RC4 Stream cipher
# Order of arguments: key-size key-file input-file output-file operation
def RC4(keySize, keyFile, inputFile, outputFile, operation):
    if (operation == "encrypt"):
        # Open the key file and store the key 
        f = open(keyFile, 'r+b')
        # f = open(keyFile)
        key = f.read()
        f.close()

        # Open the input file as binary
        f = open(inputFile, 'r+b')
        plaintext = f.read()
        f.close()

        # Get the keystream
        getKeystream(key)

        cipher = ""

        # Encrypt the plaintext
        for c in plaintext:
            cipher += plaintext ^ key.next()

        # Open the output file
        f = open(outputFile, 'w+b')
        # byte_arr = [120, 3, 255, 0, 100]
        # binary_format = bytearray(byte_arr)
        # f.write(binary_format)
        # keystream.to_bytes()
        f.write(key)
        f.close()

def getKeystream(key):
    s = KSA(key)
    keyStream = PRGA(s)
    # Throw away the first 3072 bits
    for i in range(3072):
        next(keyStream)
    return keyStream

# Key-scheduling algorithm
def KSA(key):
    # for i from 0 to 255
    s = list(range(256))
    keySize = len(key)

    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keySize]) % 256
        s[i], s[j] = s[j], s[i]

    return s

# Pseudo-random generation algorithm
def PRGA(s):
    i = 0
    j = 0

    while 1:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        K = s[(s[i] + s[j]) % 256]
        yield K

RC4(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
