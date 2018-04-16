from ciphers import Cipher
import string
from helper import mod_inv
class Affine(Cipher):
    """Class that implements affine cipher method"""


    def __init__(self):
        
        self.alphabetList = list(string.ascii_uppercase)
        self.m = len(self.alphabetList)
    
    def encrypt(self,text,a,b):
        """A method that encrypts a message according to the affine cipher"""

        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabetList.index(char)
            except ValueError:
                output.append(char)
            else:
                result = (a*index+b)%self.m
                output.append(self.alphabetList[result])
        return ''.join(output)
    #Method to decrypt a message
    def decrypt(self, text,a,b):
        """A method that decrypts a message according to the affine cipher"""

        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabetList.index(char)
            except ValueError:
                output.append(char)
            else:
                result = (mod_inv(a,self.m)*(index-b))%self.m
                output.append(self.alphabetList[result])
        return ''.join(output)
    
