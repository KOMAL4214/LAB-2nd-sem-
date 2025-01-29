print("program of rfind")
string=input("enter the string :")
substring=input("enter the sub string to be find :")
k=0
for i in range(1,len(string)-len(substring)+2) :
    if(string[-(i+len(substring)-1):-i]+string[-i]==substring) :
        k=i+len(substring)-1
if(k==0) :
    print("return -1")
else :
     print(len(string)-k)