# Ciphers
Python files that implement different types of ciphers
In order to run this file you need to use the command prompt or terminal and be in the same directory as the files. Once you have navigated to the folder where the python files are located you simply need to run "python interface.py", after which you will prompted to enter the message you want to encrypt or decrypt.
Afterwards, you will be asked to provide a one time pad key. This key should be the same length as the message.
Then you will be prompted whether you want to encrypt or decrypt the message
Then you have to choose the method to encrypt or decrypt. It can be either "Atbash", "Affine", or "Hill.

If you want to learn more about the atbash cipher, navigate to this link: https://en.wikipedia.org/wiki/Atbash

If you want to learn more about the affine cipher, navigate to this link: https://en.wikipedia.org/wiki/Affine_cipher?wprov=srpw1_0

If you want to know more about the hill cipher, navigate to this link: https://en.wikipedia.org/wiki/Hill_cipher

Unless you chose the Atbash method you will have to provide a key. In the case of Affine you provide two integer keys. In the case of the Hill cipher you provide a matrix in the form of a numpy array (even if it is just one digit).
