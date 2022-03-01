# Created with Python 3.10.0
# CS4640 Homework #2 RC4 cipher

import sys

# RC4 Stream cipher
# Order of arguments: key-size key-file input-file output-file operation
def RC4(keySize, keyFile, inputFile, outputFile, operation):
    if (operation == "encrypt"):
        # Open the key file and store the key 
        f = open(keyFile, 'r+b')
        key = f.read()
        f.close()

        # Open the input file as binary
        f = open(inputFile, 'r+b')
        plaintext = f.read()
        f.close()   

        # Get the keystream
        s = KSA(key)
        keyStream = PRGA(s, plaintext)
        # Throw away the first 3072 bits
        keyStream[3072:]

        print("keystream: ")
        print(keyStream)
        print("plaintext: ")
        print(plaintext)

        # Encrypt the plaintext
        cipher = []
        for i in range(len(plaintext)):
            x = keyStream[i] ^ plaintext[i]
            cipher.append(x)

        print("ciphertext:")
        print(cipher)

        # Open the output file
        f = open(outputFile, 'w+b')
        binary_format = bytearray(cipher)
        f.write(binary_format)

        # f.write(key)
        f.close()

    if (operation == "decrypt"):
        # Open the key file and store the key 
        f = open(keyFile, 'r+b')
        key = f.read()
        f.close()

        # Open the input file as binary
        f = open(inputFile, 'r+b')
        ciphertext = f.read()
        f.close()

        # Get the keystream
        s = KSA(key)
        keyStream = PRGA(s, ciphertext)
        # Throw away the first 3072 bits
        keyStream[3072:]

        print("keystream: ")
        print(keyStream)
        print("plaintext: ")
        print(ciphertext)

        # Decrypt the ciphertext
        plaintext = []
        print(len(ciphertext))
        print(len(keyStream))

        for i in range(len(ciphertext)):
            x = keyStream[i] ^ ciphertext[i]
            plaintext.append(x)

        print("plaintext:")
        print(plaintext)

        # Open the output file
        f = open(outputFile, 'w+b')
        binary_format = bytearray(plaintext)
        f.write(binary_format)
        f.close()

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
def PRGA(s, plaintext):
    i = 0
    j = 0
    keystreamList = []

    for p in plaintext:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        keystreamList.append(k)
        # print(keystreamList)
    
    return keystreamList

RC4(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
