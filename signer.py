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
		# getFileSig = computes the SHA512 hash and encrypts it with the private key 
		fileSignature = getFileSig(inputFileName, privateKey)
		
		# Saving the digital signature to sigFileName
		saveSig(sigFileName, fileSignature)

		# Notify the user that the signature was saved to the file
		print("Succes! Saved the signature of", inputFileName, "to", sigFileName)
	
	elif mode == "verify":
		# Reading the public key from a .pem file
		publicKey = loadKey(keyFileName)

		# Getting the saved signature from file and storing it in digitalSig
		digitalSig = loadSig(sigFileName)
		
		# Comparing the decrypted value against the SHA512 hash
		# verifyFileSig decrypts the signature with the publicKey
		verifyFileSig(inputFileName, publicKey, digitalSig)
	else:
		print("Invalid mode, please try again.")
		exit()


if __name__ == "__main__":
	main()
