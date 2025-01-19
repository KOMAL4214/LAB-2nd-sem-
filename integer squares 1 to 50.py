print("program to get a list of 'a' to 'zzz...z'")
list=[]
x=1
for i in range (0,26) :
    list.append(chr(97+i)*(i+1))
print(list)