import os, random, struct
import sys
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode 

##################################################
# Loads the RSA key object from the location
# @param keyPath - the path of the key
# @return - the RSA key object with the loaded key
##################################################
def loadKey(keyPath):
	# The RSA key
	key = None
	
	# Open the key file
	with open(keyPath, 'r') as keyFile:
		# Read the key file
		keyFileContent = keyFile.read()
		# Decode the key
		decodedKey = b64decode(keyFileContent)
		# Load the key
		key = RSA.importKey(decodedKey)
		
	# Return the key
	return key	
		
##################################################
# Signs the string using an RSA private key
# @param sigKey - the signature key
# @param string - the string
# @return digSignature - the digital signature
##################################################
def digSig(sigKey, string):
	# Get the SHA-512 hash of the string data
	dataHash = SHA512.new(string).hexdigest()
	
	# Generating the signature by encrypting our hash with the private key
	digSignature = sigKey.sign(dataHash, '')
	
	# Returning the digital signature
	return digSignature

##########################################################
# Returns the file signature
# @param fileName - the name of the file
# @param privKey - the private key to sign the file with
# @return fileSig - the file signature
##########################################################
def getFileSig(fileName, privKey):
	# TODO:
	# Open the input file and read contents
	data = None
	data = open(fileName, "r")
	if data.mode == "r":
		datainFile = data.read()
	
	# Encrypting the contents with DES using 98765432 as my key
	des = DES.new('98765432', DES.MODE_ECB)
	cipherData = des.encrypt(datainFile)
	
	# Compute the SHA-512 hash of the contents
	# dif = data in file 
	difHash = SHA512.new(cipherData).hexdigest()
	
	# Creating the signature for the input file with the 
	# hash using the digSig() function
	fileSig = digSig(privKey, difHash)
	
	# Closing the file 
	data.close()
	
	# Return the signature
	return fileSig
	
###########################################################
# Verifies the signature of the file
# @param fileName - the name of the file
# @param pubKey - the public key to use for verification
# @param signature - the signature of the file to verify
##########################################################
def verifyFileSig(fileName, pubKey, signature):
	
	# TODO:
	# 1. Read the contents of the input file (fileName)
	# 2. Compute the SHA-512 hash of the contents
	# 3. Use the verifySig function you implemented in
	# order to verify the file signature
	# 4. Return the result of the verification i.e.,
	# True if matches and False if it does not match
	
	pass

############################################
# Saves the digital signature to a file
# @param fileName - the name of the file
# @param signature - the signature to save
############################################
def saveSig(fileName, signature):

	# TODO: 
	# Signature is a tuple with a single value.
	# Get the first value of the tuple, convert it
	# to a string, and save it to the file (i.e., indicated
	# by fileName)
	
	# Getting the first value of the tuple
	signature_tuple = ast.literal_eval(signature)
	
	# Converting the tuple into a string
	sigtupString = ''.join(signature_tuple)
	
	# Saving the tuple into the file
	savetoFile = None
	savetoFile = open(fileName, "w+")
	savetoFile.write(sigtupString)
	
	# Closing the file
	savetoFile.close()

###########################################
# Loads the signature and converts it into
# a tuple
# @param fileName - the file containing the
# signature
# @return - the signature
###########################################
def loadSig(fileName):
	
	# TODO: Load the signature from the specified file.
	# Open the file, read the signature string, convert it
	# into an integer, and then put the integer into a single
	# element tuple
	
	pass
	
#################################################
# Verifies the signature
# @param theHash - the hash 
# @param sig - the signature to check against
# @param veriKey - the verification key
# @return - True if the signature matched and
# false otherwise
#################################################
def verifySig(theHash, sig, veriKey):
	
	# TODO: Verify the hash against the provided
	# signature using the verify() function of the
	# key and return the result
	pass			



# The main function
def main():	
	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print ("USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
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
	
	# TODO: Load the keys using the loadKey() function provided.
	if keyFilename == "pubKey.pem":
		publicKey = loadKey(keyFileName)
	elif keyFilename == "privKey.pem":
		privateKey = loadKey(keyFileName)
	
	# We are signing
	if mode == "sign":
		# TODO: 1. Get the file signature
		#       2. Save the signature to the file
		
		# Getting the digital signature for the input file
		fileSignature = getFileSig(inputFileName, privateKey)
		
		# Saving the digital signature to sigFileName
		saveSig(sigFileName, fileSignature)
		
		# Notify the user that the signature was saved to the file
		print ("Succes! Signature saved to file: ", sigFileName)
	# We are verifying the signature
	elif mode == "verify":
		
		# TODO Use the verifyFileSig() function to check if the
		# signature signature in the signature file matches the
		# signature of the input file
		print ("Success! Signatures match.")
		print ("Error! Signatures do not match.")
	else:
		print ("Invalid mode, please try again.")

### Call the main function ####
if __name__ == "__main__":
	main()
