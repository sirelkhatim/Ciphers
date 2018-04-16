import string
from ciphers import Cipher

class Atbash(Cipher):
    """Class that implements atbash cipher method"""


    def __init__(self):

        self.alphabetList = list(string.ascii_uppercase)
    
    def encrypt(self,text):
        """A method that encrypts a message according to the atbash cipher"""

        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabetList.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alphabetList[-(index+1)])
        return ''.join(output)
    
    def decrypt(self, text):
        """A method that decrypts a message according to the atbash cipher"""
        
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabetList.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alphabetList[-(index+1)])
        return ''.join(output)
