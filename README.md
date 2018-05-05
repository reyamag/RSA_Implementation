# RSA_Implementation
An implementation of RSA public key cryptography using Python's cryptographic libraries.

# Authors
Charles Bucher: charles.abucher@gmail.com <br>
Reyniel Maglian: rrmaglian@csu.fullerton.edu

# Instructions
Our goals are to design an application for creating and verifying file signatures, utilize RSA public key encryption algoritm, and experiement with Python's cryptographic libraries.

We will utilize RSA public key encryption to implement a utility for creating and verifying digital signatures of files.

When the program is running, it will check the mode, if the mode is sign, the program will read the private key from the specified .pem file, generate and use SHA 512 to compute the has of the file's contents, encrypt the output of SHA 512 using the rSA private key and write the resulting signature to the signature file. 

If the mode is verify, the program will read the public key from the specified .pem file, read the signature from the specifed signature file, and compute the SHA 512 hash of the data file's contents. Next it will decrypt the signature and compare the result against the SHA 512 hash. If they match, then the signature has been successfully verified. If they do not match, then the verifircation fails. The program will utput the result of the verification. 

# Running the program
python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE> 
  Where, 
    KEY FILE NAME: the name of the file containing the private key (if signing) or public key
    SIGNATURE FILE NAME: the file to which to save the digital signature (if signing) or from which to load the digital sigature (when verifiying)
    INPUT FILE NAME: the file for which to generate or verify the digital signature
    MODE: Can be the following,
        sign:
        1. read input file name
        2. compute an SHA 512 hash of the contents read
        3. encrpyt the hash with the private key from the key file name file
        4. save the result (the digital signature) to the signature file name
        verify:
        1. read the input file name
        2. compute an SHA 512 hash of the contents read
        3. decrypt the signature from signature file name using the public key from file key file name
        4. compare the decrypted vale against the SHA 512 hash, and output whether the signature matches.
  
