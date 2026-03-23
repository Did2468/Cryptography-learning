import random 
import math 



def prime_checker(n):
    count = 0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            count = 1
            break
    if(count == 0):
        return 1
    else:
        return 0

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(e, phi):
    gcd, x, _ = egcd(e, phi)
    if gcd != 1:
        raise Exception("Inverse doesn't exist")
    return x % phi



test=1      #get value of p
while(test):
    p=random.randint(1,1000000)
    if(prime_checker(p)):
        test=0
test=1                  #get value of q
while(test):
    q=random.randint(1,1000000)
    if(prime_checker(q)):
        test=0

n = p*q

phi = (p-1) * (q-1)

test = 1

while(test):            #get value of e
    e = random.randint(1,phi)
    if(math.gcd(e,phi)==1):
        test=0

d = mod_inverse(e,phi)      #get value of d


print("Value of n is: ",n)
print("Value of e is: ",e)
print("Value of d is: ",d)
