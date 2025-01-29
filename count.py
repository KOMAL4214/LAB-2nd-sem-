print("program to count")
string=input("enter the string :")
sub=input("enter the string part which should be counted :")
k=0
for i in range(0,len(string)-len(sub)+1) :
    if(string[i:i+len(sub)]==sub) :
        k+=1
print("this part repeated ",k," times")
            