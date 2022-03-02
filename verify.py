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
    for chunk in reverse(f, inputSize, lastChunkSize):
        # Create new hash for each chunk, and append
        h = SHA256.new()
        h.update(chunk)
        if(h0):
            h.update(h0)
        h0 = h.digest()
    f.close()

    # Compare the given hash to the calculated hash
    if (hash == h0.hex()):
        print("True")
    else:
        print("False")


def reverse(f, fileSize, lastChunkSize):
	x = 0
	y = fileSize
	while y > 0:
		size = 4096
		if(x == 0):
			size = lastChunkSize
        # Offset file search
		f.seek(y - size)
		chunk = f.read(4096)
		if not chunk:
			break
		x = x + 1
		y -= size
        # Return the chunk
		yield chunk

verify(sys.argv[1], sys.argv[2])
