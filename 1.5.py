names=[]
for i in range(0,10) :
    names.insert(i,input("enter your name :"))
    names[i]=names[i][::-1]
print(names)
