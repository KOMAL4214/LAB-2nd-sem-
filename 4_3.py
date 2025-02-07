alphabets=[chr(i) for i in range (97,123)]
str=input("enter the string : ")
str=list(str)
for i in range(0,26):
    if(alphabets[i] not in str):
        print("not palagram")
        break
    elif(i==25):
        print("palagram")