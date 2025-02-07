t=int(input("enter the number of testcases :"))
while(t>0):
    l=[]
    k=0
    low=int(input("enter the lower value :"))
    high=int(input("enter the higher value :"))
    for i in range (0,high+1):
        l.append(i**2)
    for i in range (low,high+1):
        if(i in l):
            k+=1
    print(k)
    t-=1
    