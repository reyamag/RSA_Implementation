all:
	@cp signer.py
  @cp signingFunctions.py

clean:  
  @rm -f signer.py
	@rm signingFunctions.py
