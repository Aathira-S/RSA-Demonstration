#primenos.py
#FINAL VERSION WITH DOUMENTATION

'''
creates file primenos.txt and
inserts 1-4 digit prime
prime numbers are generated using sieve method
'''


file=open("primenos.txt","w") #creating file object

#create a list containing keyword False in all indexes
#except 0 and 1 where value is True
l=[True if i>1 else False for i in range(10001)] 

#using sieve method to generate prime numbers
p =2
while p**2 <=10000:
    if l[p]==True:
     for i in range(p**2,10000+1,p): #iterating from p^2 to 10,000
        l[i]=False #positions of composite numbers assigned value False
    p+=1
    
prime=[] #list containg primes
for i,n in enumerate(l):
    if n:
        prime+=[str(i)+'\n'] #appending list with prime numbers
        
file.writelines(prime) #writing prime numbers into file
file.close()
