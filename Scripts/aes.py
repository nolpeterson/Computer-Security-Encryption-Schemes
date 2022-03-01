# Created with Python 3.10.0
# CS4640 Homework #2 AES cipher - CTR mode

import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Set all input arguments
keySize = sys.argv[1]
keyFile = sys.argv[2]
inputFile = sys.argv[3]
outputFile = sys.argv[4]
operation = sys.argv[5]

# AES cipher
# Order of arguments: key-size key-file input-file output-file operation
# def AES(keySize, keyFile, inputFile, outputFile, operation): Unable to put in function def due to crypto library

# Encrypt
if (operation == "encrypt"):
    # Open the key file and store the key 
    f = open(keyFile, 'r')
    key = f.read()
    f.close()

    # Conver the key to bytes
    key = int(key, 2).to_bytes(len(key) // 8, byteorder="big")

    # Open the input file as binary
    f = open(inputFile, 'r+b')
    plaintext = f.read()
    f.close()   

    # Output the plaintext
    print("plaintext: ")
    print(plaintext)

    # Encrypt the plaintext
    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    n = cipher.nonce

    # Output the nonce
    print("nonce:")
    print(n)

    # Output the resulting ciphertext
    print("ciphertext:")
    print(ciphertext)

    # Open the output file and write the ciphertext
    f = open(outputFile, 'w+b')
    f.write(n)
    f.write(ciphertext)
    f.close()

# Decrypt
if (operation == "decrypt"):
    # Open the key file and store the key 
    f = open(keyFile, 'r')
    key = f.read()
    f.close()

    # Conver the key to bytes
    key = int(key, 2).to_bytes(len(key) // 8, byteorder="big")

    # Open the input file as binary
    f = open(inputFile, 'r+b')
    # Store the first 8 bits as the nonce
    n = f.read(8)
    ciphertext = f.read()
    f.close()

    # Decrypt the ciphertext
    cipher = AES.new(key, AES.MODE_CTR, nonce=n)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Output the cipher text
    print("ciphertext: ")
    print(ciphertext)

    # Output the resulting plaintext
    print("plaintext:")
    print(plaintext)

    # Open the output file
    f = open(outputFile, 'w+b')
    f.write(plaintext)
    f.close()
