print("program to replace")
l=[]
string=input("enter the string :")
sub=input("enter the string part where it should be replaced :")
replace=input("enter the  replacing string :")
for i in range(0,len(string)-len(sub)+1) :
    if(string[i:i+len(sub)]==sub) :
            l.append(string[0:i]+replace+string[i+len(sub):])
print(l[0])