message = eval(input("Enter the the message to be decrypted:"))
d = int(input("Enter the value of d:"))
n = int(input("Enter the value of n:"))

def decrypt(message):
    dec = []
    for i in range(len(message)):
        decc = pow(message[i],d,n)
        asci = chr(decc)
        dec.append(asci)
    return dec

decrypted = decrypt(message)

print("The decrypted message is: ")
for i in decrypted:
    print(i,end="")
print()
