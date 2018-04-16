class Cipher:

    def __init__(self):
        
        self.alphabetList = list(string.ascii_uppercase)
        self.m = len(self.alphabetList)

    def encrypt(self):
    	"""A method to encrypt a message"""
    	
        raise NotImplementedError()

    def decrypt(self):
    	"""A method to decrypt a message"""

        raise NotImplementedError()




