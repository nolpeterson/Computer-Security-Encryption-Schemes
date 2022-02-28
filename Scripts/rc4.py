# Created with Python 3.10.0
# CS4640 Homework #2 RC4 cipher

import sys

# RC4 Stream cipher
# Order of arguments: key-size key-file input-file output-file operation
def RC4(keySize, keyFile, inputFile, outputFile, operation):
    # if (operation == "encrypt"):
    #     key = keyFile
    # f = open(inputFile)
    # lines = f.read()
    # lines
    # f.close()
    f = open('my_file', 'w+b')
    byte_arr = [120, 3, 255, 0, 100]
    binary_format = bytearray(byte_arr)
    f.write(binary_format)
    f.close()

RC4(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
