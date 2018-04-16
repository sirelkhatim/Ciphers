#Load classes and packages needed
from helper import mod_mat_inv, is_invertible
from hill import Hill
from atbash import Atbash
from affine import Affine
from onepad import OnePad
import numpy as np
from helper import mod_mat_inv, exit_program, encrypt_decrypt


#Create interface for users to interact with program
if __name__=="__main__":
    #Get message and one time pad from user
    msg = input("Please enter the message to encrypt or decrypt: ")
    exit_program(msg)
    one_pad = input("Please enter your one-time pad key ")
    #Check that one time pad and message are same size
    while len(one_pad) != len(msg):
        #Check if user typed exit
        exit_program(one_pad)
        one_pad = input("One-time pad must have the same number of characters as the message. Please try again: ")

    #Find out whether the user wants to encrypt or decrypt the message  
    option = input("Please enter 'encrypt' or 'decrypt'. You can exit the program by typing 'exit': ")
    msg = msg.lower()
    option= option.lower()
    #Check for right input in option
    while option!="encrypt" and option!="decrypt":
        exit_program(option)
        option = input("Please enter encrypt or decrypt: ")

    print("############################################################")
    print("What method of encryption/decryption would you like to use?")
    print("############################################################")
    print("The choices are 'atbash', 'affine', and 'hill'")
    print("############################################################")

    #Get the cipher method the user wants to use
    cipher_method = input("Please enter the method: ")
    #Convert message and option, and cipher method to lowercase

    cipher_method= cipher_method.lower()
        

    #use OTP (one-time pad) to encrypt the message if the user wants to encrypt
    onetime= OnePad()
    if option=='encrypt':
        msg = onetime.encrypt(msg,one_pad)

    #Check that the user hasn't typed an invalid cipher method
    while cipher_method not in ["affine", "hill", "atbash"]:
        exit_program(cipher_method)
        cipher_method = input("Please enter a valid method: ")

    #Check which cipher method the user wants
    if cipher_method == "atbash":
        atbash = Atbash()
        #Encrypt or decrypt according to the users choice
        result = encrypt_decrypt(atbash, msg,option = option)

    elif cipher_method=="affine":
        key1 = input("please enter the key a here: ")
        exit_program(key1)
        key2 = input("enter the key b here: ")
        exit_program(key2)
        try:
            key1 = eval(key1)
            key2 = eval(key2)
        except:
            while type(key1)!=int and type(key2)!=int:
                key1 = input("Key must be an integer. please enter the key a here: ")
                key2 = input("Key must be an integer. enter the key b here: ")
                try:
                    key1 = eval(key1)
                    key2 = eval(key2)
                except:
                    continue

        affine = Affine()
        result = encrypt_decrypt(affine, msg,option,key1,key2)

    else:
        condition = True
        while condition:
            try:
                key = input("please enter the key here: (Use np.array to enter your key. The matrix must be a square matrix. For example the identity matrix is np.array([[1,0],[0,1]])) ")
                if key == 'exit':
                    sys.exit(1)
                key = eval(key)
                while type(key) != type(np.array([1,2])):
                    print("The key must be defined as a numpy array ")
                    key = input("Please enter a numpy array as a key: ")
                    if key.lower() == 'exit':
                        sys.exit(1)
                    key = eval(key)
                check = len(msg)%key.shape[1]
                while not is_invertible(key):
                    print("You have not entered a valid key. The key must be a K-square invertible matrix, where K is a factor of the length of the message. ")
                    key = input("The matrix you entered is not invertible. please enter the key here: ")
                    if key.lower() == 'exit':
                        sys.exit(1)
                    key = eval(key)
                if check==0:
                    condition = False

            except NameError:
                "You have not entered a valid key. The key must be a K-square invertible matrix, where K is a factor of the length of the message. "
                key = input("please enter the key here: ")
                if key.lower() == 'exit':
                    sys.exit(1)
                key = eval(key)
                check = len(msg)%key.shape[1]
                if check==0:
                    condition = False               


        hill = Hill()
        result = encrypt_decrypt(hill, msg,option,key)
    #Finally after decrypting the message you must remove the one-time pad so you can get the original message
    if option == "decrypt":
        result = onetime.decrypt(result,one_pad)
        print("Your decrypted message is: ", result)



