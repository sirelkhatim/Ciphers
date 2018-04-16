### Helper functions ###
import numpy as np
import sys

def mod_mat_inv(A,p):       # Finds the inverse of matrix A mod p
    """ A function that finds the inverse of a matrix A mod p"""

    n=len(A)
    A=np.matrix(A)
    adj=np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p
    return (mod_inv(int(round(np.linalg.det(A))),p)*adj)%p

def mod_inv(a,p):
    """  A function that finds the inverse of a integer a"""

    for i in range(1,p):
        if (i*a)%p==1: return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):
    """ Function that return matrix A with the ith row and jth column deleted """

    A=np.array(A)
    minor=np.zeros(shape=(len(A)-1,len(A)-1))
    p=0
    for s in range(0,len(minor)):
        if p==i: p=p+1
        q=0
        for t in range(0,len(minor)):
            if q==j: q=q+1
            minor[s][t]=A[p][q]
            q=q+1
        p=p+1
    return minor


def is_invertible(key):
    """checks if a matrix is invertible"""
    try:
        mod_mat_inv(key,26)
        return True
    except:
        return False

def exit_program(txt):
    if txt.lower() == 'exit':
        sys.exit(1)

def encrypt_decrypt(cipher, txt,option,*args):
    if option == "encrypt":
        result = cipher.encrypt(txt,*args)
        print("Your encrypted message is: ", result )
    if option == "decrypt":
        result = cipher.decrypt(txt,*args)
        return result