from ciphers import Cipher
import string
import numpy as np
from helper import mod_mat_inv


class Hill(Cipher):
	"""Class that encrypts and decrypts text according to the Hill cipher"""


	def __init__(self):

		self.alphabetList = list(string.ascii_uppercase)
		self.m = len(self.alphabetList)

	def encrypt(self,text,key1):
		"""method that encrypts a text according to the hill cipher"""

		output = []
		code = []
		finalCode = []
		text = text.upper()
		for char in text:
			try:
				index = self.alphabetList.index(char)
			except ValueError:
				code.append(char)
			else:
				code.append(index)
		arrayCode = np.array(code)
		for i in np.split(arrayCode,len(text)//key1.shape[1]):
			finalCode.append(np.dot(key1,i)%self.m)
		for c in finalCode:
			for j in c:
				output.append(self.alphabetList[int(j)])
		return ''.join(output)

	def decrypt(self, text,key1):
		"""method that decrypts a text according to the hill cipher"""

		output = []
		code = []
		final_code = []
		text = text.upper()
		for char in text:
			try:
				index = self.alphabetList.index(char)
			except ValueError:
				code.append(char)
			else:
				code.append(index)
		arrayCode = np.array(code)
		for i in np.split(arrayCode,len(text)//key1.shape[1]):
			final_code.append(np.dot(mod_mat_inv(key1,26),i)%self.m)
		for c in final_code:
			for j in c:
				output.append(self.alphabetList[int(j)])
		return ''.join(output)