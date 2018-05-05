# RSA_Implementation
An implementation of RSA public key cryptography using Python's cryptographic libraries.

# Authors
Charles Bucher: charles.abucher@gmail.com <br>
Reyniel Maglian: rrmaglian@csu.fullerton.edu

# Instructions

File assig3skeleton.zip archive provides a program skeleton and les with examples of how
to generate and verify signatures.
 skeleton.py: The le where the main program is to be implemented. The use of the
skeleton le is optional.
 sha512.py: This le contains the code illustrating how to compute the hash a 512-bit
digest (i.e., hash) of any data using the SHA-512 algorithm (running: python sha512.py).
 signandverify.py: contains a simple example of generating and verifying digital signa-
tures using RSA (running: python signandverify.py).
 pubKey.pem: The le containing a sample public key.
 privKey.pem: The le containing a sample private key.
Your nished program shall be called signer.py, shall integrate both DES and shall be executed
as:
python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>
Each parameter is dened as follows:
1
 KEY FILE NAME The name of the le containing private key (if signing) or public key (when
verifying the digital signature).
 SIGNATURE FILE NAME: The le to which to save the digital signature (if signing) or from
which to load the digital signature (when verifying).
 INPUT FILE NAME: The le for which to generate or verify the digital signature.
 MODE: Can be one of the following:
{ sign: This mode tells the program to:
1. Read the INPUT FILE NAME
2. Compute an SHA-512 hash of the contents read
3. Encrypt the hash with the private key from KEY FILE NAME le
4. Save the result (i.e., the digital signature) to the SIGNATURE FILE NAME.
{ verify: This mode tells the program to:
1. Read the INPUT FILE NAME.
2. Compute an SHA-512 hash of the contents read
3. Decrypt the signature from SIGNATURE FILE NAME using the public key from
le KEY FILE NAME
4. Compare the decrypted value against the SHA-512 hash, and output whether the
signature matches.To add.

# Additional

To add.
