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
		
	# Compute the SHA-512 hash of the contents
	# dif = data in file 
	difHash = SHA512.new(datainFile).hexdigest()

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
	inputData = None
	inputData = open(fileName, "r")
	if inputData.mode == "r":
		inputdataContents = inputData.read()
		
	# 2. Compute the SHA-512 hash of the contents
	# idc = input data contents
	idcHash = SHA512.new(inputdataContents).hexdigest()
	
	# 3. Use the verifySig function you implemented in
	# order to verify the file signature
	result = verifySig(idcHash, signature, pubKey)
	
	# 4. Return the result of the verification i.e.,
	# True if matches and False if it does not match
	if result == True: 
		print("Success! Signatures match.")
	elif result == False:
		print("Error! Signatures DO NOT match.")

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
	
	# Getting the tuple with a single value
	sigTuple = (signature,)
	
	# Converting the tuple into a string
	sigtupString = " ".join([str(x[0]) for x in sigTuple])
	
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
	
	# Opening the file and reading the signature
	sig = None
	sig = open(fileName, "r")
	if sig.mode == "r":
		signatureinFile = sig.read()
		
	# Converting the signature into an integer single element tuple
	singleElemTuple = tuple(map(int, signatureinFile.split(' ')))
	
	return singleElemTuple
	
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
	
	# Verifying the has against the signature 
	verifyingObject = PKCS1_v1_5.new(veriKey.publickey())
	verified = verifyingObject.verify(theHash, sig)
	
	# Returning the result 
	if verified == True:
		return True
	else:
		return False

	

################################################
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
	
	#**********TODO at the end: DES encryption on the data
	# Opening the input file and reading the data
	#data = None
	#data = open(inputFileName, "r")
	#if data.mode == "r":
	#	datainFile = data.read()
	
	# Encrypting the data contents with DES using 98765432 as my key
	# dif = data in file
	#des = DES.new('98765432', DES.MODE_ECB)
	#difEncrypted = des.encrypt(datainFile)
	
	# We are signing
	if mode == "sign":		
		# Reading the private key from a .pem file
		privateKey = loadKey(keyFileName)
		
		# Getting the digital signature for the input file
		fileSignature = getFileSig(inputFileName, privateKey)
		
		# Saving the digital signature to sigFileName
		saveSig(sigFileName, fileSignature)
		
		# Notify the user that the signature was saved to the file
		print "Succes! Saved the signature of", inputFileName, " to", sigFileName
	# We are verifying the signature
	elif mode == "verify":
		# Reading the public key from a .pem file
		publicKey = loadKey(keyFileName)
		
		# Reading the signature from sig file
		digitalSig = loadSig(sigFileName)
		
		# Decrypt the signature and compare the result against the SHA512 hash
		verifyFileSig(inputFileName, publicKey, digitalSig)
	else:
		print "Invalid mode, please try again."
		exit()

### Call the main function ####
if __name__ == "__main__":
	main()
