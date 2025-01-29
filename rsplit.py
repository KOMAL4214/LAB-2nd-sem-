print("program to rsplit")
string=input("enter the string :")
split=input("enter the string that must be splited :")
l=[]
for i in range(1,len(string)+1) :
    if(string[-(i+len(split)-1):-i]+string[-i]==split) :
        l.append(string[-(len(string)):-(i+len(split)-1)])
        if(i!=1) :
            l.append(string[-i+1:])
        else :
            l.append('')
print(l)

