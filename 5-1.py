l=int(input("enter the number :"))
r=int(input("enter the number :"))
k=[]
for i in range (l,r+1) :
    for j in range (i,r+1):
        k.append(i^j)
print(max(k))