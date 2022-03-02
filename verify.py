# Created with Python 3.10.0
# CS4640 Homework #2 Verify the integrity of a file

from Crypto.Hash import SHA256
import sys
import os

# Order of arguments: input-pdf-file original-hash-value
def verify(inputFile, hash):
    # Find the sizes of the chunks
    inputSize = os.path.getsize(inputFile)
    lastChunkSize = inputSize %  4096

    f = open(inputFile, 'rb')
    h0 = ""
    for chunk in reverse(f, inputSize, lastChunkSize, 4096):
        h = SHA256.new()
        h.update(chunk)
        if(h0):
            h.update(h0)
        h0 = h.digest()
    f.close()

    if (hash == h0.hex()):
        print("True")
    else:
        print("False")

	# Return the last hash (h0)
    # return last_hash
    # calculatedHash = calculate_hash(inputFile, blockSize)
    # print(calculatedHash.hex())
    # if (hash == calculatedHash.hex()):
    #     print("True")
    # else:
    #     print("False")

def reverse(file_object, file_size, last_chuck_size, chunk_size):
	iter = 0
	lastPos = file_size
	while lastPos > 0:
		size = chunk_size
		if(iter == 0):
			size = last_chuck_size

		file_object.seek(lastPos - size)
		data = file_object.read(chunk_size)
		if not data:
			break

		iter = iter + 1
		lastPos -= size
		yield data

verify(sys.argv[1], sys.argv[2])
