message = input("Enter the message to be encrypted: ")

e = int(input("Enter the value of e: "))
n = int(input("Enter the value of n: "))

def encrypt(message):
    encryption = []
    for i in range(len(message)):
        asci = ord(message[i])
        enc = pow(asci,e,n)
        encryption.append(enc)
    return encryption

encrypted = encrypt(message)

print(encrypted)
