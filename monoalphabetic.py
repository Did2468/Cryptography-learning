import random

def randomgen(upper):
    return random.randint(0,upper)

def create():
    transform = dict()

    keyboard = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.',',','!','@','#','$','%','&','+','-','*','/','_',':','[',']','(',')',' ','=','{','}',"'",'"',';','1','2','3','4','5','6','7','8','9','0']

    taken_s=[]
    n = len(keyboard)
    print("creating the keys")

    for i in range(n):
        while(1):
            r = randomgen(n-1)
            if(keyboard[r] not in taken_s):
                taken_s.append(keyboard[r])
                transform[keyboard[i]] = keyboard[r]
                break

    return transform

def process(line,data):
    print("in the process stage")
    mod = ""
    for char in line:
        if(char == "\n"):
            mod += "\n"
            continue
        mod += data[char]
    return mod


def main():
    data = create()
    with open("file.txt", "r") as fin, open("output.txt", "w") as fout:
        for line in fin:
            modified_line = process(line,data)
            # write processed data
            fout.write(modified_line)

    print("sucesfully created")
    print(data)

if __name__ == "__main__":
    main()



