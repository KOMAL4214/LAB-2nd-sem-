k0=[]
k1=[]
k2=[]
k3=[]
k4=[]
for i in range (0,10000) :
    l=(i+1)%5
    if(l==0) :
        k0.append(l)
    elif(l==1) :
        k1.append(l)
    elif(l==2) :
        k2.append(l)
    elif(l==3) :
        k3.append(l)
    elif(l==4) :
        k4.append(l)
list={0,1,2,3,4}
z=set(k0+k1+k2+k3+k4)
print("checking validity")
if(list==z):
    print("hence these are valid")