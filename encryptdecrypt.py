#FINAL VERSION WITH DOCUMENTATION
#last edited on 06/01/2020 15:35
#encryptdecrypt.py


'''
includes
- encdec function : encrypts/decrypts the list of numbers with key given
- makeblock function : makes blocks of whole string message m
- breakblock function : reconstructs the message msg from list of blocks
- encrypt function : full encryption of message string using makeblock and encdec
                     with key k
- decrypt funtion : full decryption of the ciphertext back to message using encdec
                    and breakblock using key k 
'''


def encdec(mblock,e,n):  
    '''-inputs a list of integers as mblock
        -encrpyts/decrypts each value in mblock
        -returns a list of integers called C
        corresponding to their respective
        decryptions/encryptions'''
   
    ebin=str(bin(e))[2:]    #to hold e in binary form
    #bin(val) converts to string of form 0bxxxxx where xxxxx represents the binary value of val
    
    C=[]    #to hold corresponding encrypted/decrypted values of mblock
    
    for m in mblock:
      m=int(m)
      c=1
      for i in ebin:
        c=(c**2)%n
        if i=='1':
            c=(c*m)%n       #evaluating c based on binary digit value of e
      C.append(c)       #final encrypted/decrypted value of element in mblock
            
    return C




def makeblock(m,n):
    '''breaks entire string message m into substrings of
        size based on length of n, and stores into list
        msgblock after converting to number for each
        substring using ascii number
        '''

    lenn=len(str(n))
    
    msgblock=[]
    
    size=(lenn-1)//3   #size==> determines number of characters in each block 

    count=0
    while count<len(m):
        asc=''
        for i in m[count:count+size]:  
        
            a=str(ord(i))
            x=3-len(a)          #represent of each character in a block is string of length 3
            asc+='0'*x + a          #asc==> variable holding number equivalent for each block
            
        msgblock.append(int(asc))       #adding the block onto final list 
        count+=size
    return (msgblock)




def breakblock(lis,n):
    '''converts each element of list lis
        into the corresponding substring it represents
        using ascii value and concatenates the whole
        to reproduce the full message string msg
    '''
    
    msg=''   #msg==> to store final message
    
    for i in lis:
        m=''
        while i>0:
            m=chr(i%1000)+m         #takes every 3 digits of block which represents a character of message
            i=i//1000
        msg+=m              #adds the substring onto final message
        
    return msg

def encrypt(m,k):
    '''encrypts the message string m using the
    key k and encdec and makeblock function
    (user-defined) into ciphertext list content
    '''
    content=encdec(makeblock(m,k[1]),k[0],k[1])     #key k is tuple of form (e,n) ==> (k[0],k[1])
    return content


def decrypt(c,k):
    '''decrypts the ciphertext list c usinf the
        key k and encdec and breakblock functions
        (user-defined) into final message string
        final_msg
    '''
    
    final_msg=breakblock(encdec(c,k[0],k[1]),k[1])   #key k is tuple of form (e,n) ==> (k[0],k[1])
    return final_msg
        
