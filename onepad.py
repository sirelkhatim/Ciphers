from ciphers import *
import string

class OnePad(Cipher):
    """Class that implements One-time pad"""
    
    
    def __init__(self):

        self.alphabetList = list(string.ascii_uppercase)
        self.m = len(self.alphabetList)

    #Override encryption method
    def encrypt(self,msg,pad):
        """A method to encrypt that a message with the onepad cipher"""

        output = []
        #convert message and pad to uppercase letters
        msg = msg.upper()
        pad = pad.upper()
        for i in range(len(msg)):
            try:
                #Find index of characters for both method and pad
                index = self.alphabetList.index(msg[i])
                index2 = self.alphabetList.index(pad[i])
            except ValueError:
                output.append(msg[i])
            else:
                result = (index+index2)%self.m
                output.append(self.alphabetList[result])
        return ''.join(output)

    def decrypt(self, msg,pad):
        """A method to decrypt that a message with the onepad cipher"""

        output = []
        msg = msg.upper()
        pad = pad.upper()
        for i in range(len(msg)):
            try:
                index = self.alphabetList.index(msg[i])
                index2 = self.alphabetList.index(pad[i])
            except ValueError:
                output.append(msg[i])
            else:
                result = (index-index2)%self.m
                output.append(self.alphabetList[result])
        return ''.join(output)