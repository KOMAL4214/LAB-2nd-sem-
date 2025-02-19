t=int(input("enter the number of test cases :"))
while(t>0):
    k=int(input("enter the number of times to be cut :"))
    if(k%2==1):
        print((k//2)*(k-k//2))
    else :
        print((k//2)**2)
    t-=1