# Created with Python 3.10.0
# CS4640 Homework #2 RC4 cipher

import sys

# RC4 Stream cipher
# Order of arguments: key-size key-file input-file output-file operation
def RC4(keySize, keyFile, inputFile, outputFile, operation):
    if (operation == "encrypt"):
        # key = keyFile
        key = "01010000"
        f = open(inputFile)
        lines = f.read()
        print(lines)
        f.close()
        S = KSA(key)
        return PRGA(S)

    
    # f = open('my_file', 'w+b')
    # byte_arr = [120, 3, 255, 0, 100]
    # binary_format = bytearray(byte_arr)
    # f.write(binary_format)
    # f.close()

# Key-scheduling algorithm
def KSA(keySize, key):
    # for i from 0 to 255
    S = list(range(256))

    keySize = len(key)

    keySize = int(keySize)
    print(type(key[0 % keySize]))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keySize]) % 256
        S[i], S[j] = S[j], S[i]

    return S

# Pseudo-random generation algorithm
def PRGA(S):
    i = 0
    j = 0

    while 1:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        return K

RC4(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
