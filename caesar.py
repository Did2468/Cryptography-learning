def fun(c):
    r = (c+3)%26
    return alp[r]
def getf(c):
    for i in range(len(alp)):
        if(c == alp[i]):
            return i

alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = input("Enter the text: ");

y = ""

for i in range(len(x)):
    if(x[i] == " "):
        y+=" "
        continue
    p = getf(x[i])
    y += fun(p)

print(y)

