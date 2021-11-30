#keygen.py
#FINAL VERSION WITH DOCUMENTATION

'''
Generate RSA Key pair
includes
- getpq function : choosing random primes p,q
- gcd function : returns greatest common divisor of integers a,b
- euclidgcd function : extended Euclidian algorithm to calculate d
- main function : to generate key pair using above functions
'''

import random

def gcd(a,b):
    '''
    Performs long division method to find gcd of integers a,b
    Returns gcd
    '''
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def euclidgcd(a,b):
    '''
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    in eqn gcd(a,b) = ax + by
    '''
    if b==0:
        gcd,x,y=a,1,0
    else:
        gcd,p,q=euclidgcd(b,a%b)
        x=q
        y=p-q*(a//b)
    return gcd,x,y

def getpq():
    '''
    opens file primenos.txt and
    choose two distinct numbers p,q from it and
    returns them
    '''
    fprime=open('primenos.txt','r') #creating file object
    prime=fprime.readlines() #reading file
    
    p,q=int(random.choice(prime)),int(random.choice(prime)) #choosing random primes p,q
    while p==q or p*q<127: #ensure primes are distinct and their product p*q>=127 
        q=random.choice(prime)
        
    return p,q

def main(p=0,q=0):
    '''
    generates RSA key pairs
    may take input for primes p,q or chooses randome primes
    computes RSA key pair using these primes
    returns RSA key pairs (e,n) and (d,n) as values of e,d,n
    '''
    global phi
    if p+q==0: #check if user input is given
        p,q=getpq() #else chooses random primes p,q
    n=p*q #computen
    phi=(p-1)*(q-1) #compute phi(n)
    e=3 #set deafault value of e
    while gcd(e,phi)!=1: #ensure that gcd(e,phi) is 1
        e=random.randrange(3,phi) #else choose random value of e such that 3<e<phi

    a,d,b=euclidgcd(e,phi) #getting value of d = e^(-1)
    d=d%phi #make d part of primary ring of integers (mod phi)
    return e,d,n #return key pair values

phi=0 #to store phi(n)
