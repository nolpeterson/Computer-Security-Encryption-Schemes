All problems were done in Python 3.10.0 using the PyCryptoDome library when applicable.


For problem 1, the RC4, you can run rc4.py through the terminal with the commands:
>>> python rc4.py 128 rc4_key.txt rc4_input.txt rc4_output.txt encrypt
>>> python rc4.py 128 rc4_key.txt rc4_output.txt rc4_output2.txt decrypt
Replacing the names of the key, input, and output files with whatever files you
looking to encrypt or decrypt.


For problem 2, the AES in CTR mode, you can run aes.py through the terminal with the commands:
>>>python aes.py 128 a.key a.plaintext a.ciphertext encrypt
>>>python aes.py 128 a.key a.ciphertext b.plaintext decrypt
Replacing the names of the key, input, and output files with whatever files you
looking to encrypt or decrypt.


For problem 3, the RSA encryption and decryption, you can run rsa.py through the terminal with the commands:
>>>python rsa.py encrypt 5000 53 97
Output:
<<<Ciphertext = 4139
<<<Private Key = 617, 5141
<<<Public Key = 89, 5141
Then to decrypt:
>>>python rsa.py decrypt 4139 617 5141
<<<Plaintext = 5000


For problem 4, the Integrity Verification of a File, you can run verify.py through the terminal with the commands:
>>>python verify.py in1.pdf fa07c3b6d8016ef612044188eacef
Output:
>>>True

In problem 4, the file that is invalid with the provided hash is file input3.pdf