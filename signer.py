import sys
from signingFunctions import *

def main():	
	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print ("USAGE: $python3 " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
		exit(-1)
		
	# The program file being used
	programName = sys.argv[0]
	# The key file
	keyFileName = sys.argv[1]
	# Signature file name
	sigFileName = sys.argv[2]
	# The input file name
	inputFileName = sys.argv[3]
	# The mode i.e., sign or verify
	mode = sys.argv[4]
	
	if mode == "sign":		
		# Reading the private key from a .pem file
		privateKey = loadKey(keyFileName)
		
		# Getting the digital signature for the input file
		fileSignature = getFileSig(inputFileName, privateKey)
		
		# Saving the digital signature to sigFileName
		saveSig(sigFileName, fileSignature)

		# Encrypting the signature with DES
		inFile = None
		inFile = open(sigFileName, 'r')
		sigData = inFile.read()
		
		des = DES.new('98765432', DES.MODE_ECB)
		cipherText = des.encrypt(sigData)
		linux 14.04
		inFile.close()

		# Writing the encrypted signature back to file
		outFile = None
		outFile = open(sigFileName, 'w')

		# Converting from bytes to string
		cipherText = b"cipherText".decode("utf-8")
		outFile.write(cipherText)
		
		outFile.close()

		# Notify the user that the signature was saved to the file
		print("Succes! Saved the signature of", inputFileName, "to", sigFileName)
	
	elif mode == "verify":
		# Reading the public key from a .pem file
		publicKey = loadKey(keyFileName)
		
		# Reading the encrypted signature from file
		inFile = None
		inFile = open(sigFileName, 'r')
		encSig = inFile.read()
		inFile.close()

		# Converting from string to bytes
		sigBytes = bytes(encSig, 'utf-8')	
		
		# Decrypting the encrypted signature
		des = DES.new('12345678', DES.MODE_ECB)
		decSig = des.decrypt(sigBytes)

		# Saving the decrypted back to the file
		outFile = None
		outFile = open(sigFileName, 'w')
		outFile.write(decSig)
		outFile.close()

		# Reading the decrypted signature from sig file to verify
		digitalSig = loadSig(sigFileName)
		
		# Decrypt the signature and compare the result against the SHA512 hash
		verifyFileSig(inputFileName, publicKey, digitalSig)
	else:
		print("Invalid mode, please try again.")
		exit()


if __name__ == "__main__":
	main()
