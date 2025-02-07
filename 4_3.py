t=int(input("enter the number of test cases : "))
while(t>0):
    alphabets=[chr(i) for i in range (97,123)]
    str=input("enter the string : ")
    str=list(str)
    for i in range(0,26):
        if(alphabets[i] not in str):
            print("not palagram")
            break
        elif(i==25):
            print("palagram")
    t-=1
