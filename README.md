# RSA_Implementation
An implementation of RSA public key cryptography using Python's cryptographic libraries.
Python version used: 3.6

# Authors
Charles Bucher: charles.abucher@gmail.com <br>
Reyniel Maglian: rrmaglian@csu.fullerton.edu

# Instructions
Our goals are to design an application for creating and verifying file signatures, utilize RSA public key encryption algoritm, and experiement with Python's cryptographic libraries.

We will utilize RSA public key encryption to implement a utility for creating and verifying digital signatures of files.

When the program is running, it will check the mode, if the mode is sign, the program will read the private key from the specified .pem file, generate and use SHA 512 to compute the has of the file's contents, encrypt the output of SHA 512 using the rSA private key and write the resulting signature to the signature file. 

If the mode is verify, the program will read the public key from the specified .pem file, read the signature from the specifed signature file, and compute the SHA 512 hash of the data file's contents. Next it will decrypt the signature and compare the result against the SHA 512 hash. If they match, then the signature has been successfully verified. If they do not match, then the verifircation fails. The program will utput the result of the verification. 

# Running the Program

1. *Setup<br>*
Ensure compatability with Python3.6 and support for the Python library 'Crypto'

2. *Execute*<br>
***$python3 signer.py \<KEY FILE NAME> \<SIGNATURE FILE NAME> \<INPUT FILE NAME> \<MODE>***

  
# Argument Descriptions.

\<KEY FILE NAME>: 
- The file containing the private key (if signing) or public key (if verifying)

\<SIGNATURE FILE NAME>:
- The file to which to save the digital signature (if signing) <br>
  or
- The file from which to load the digital sigature (when verifiying)
  
\<INPUT FILE NAME>: 
- The file whose contents are actually signed
  
\<MODE>: 
- Sign
- Verify
