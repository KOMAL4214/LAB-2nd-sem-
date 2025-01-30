t=int(input("enter the number of testcases :"))
while(t>0) :
    n=int(input("enter the required number :"))
    l=[]
    nxtnum=0
    n1=0
    n2=1
    l.append(n1)
    l.append(n2)
    while(n!=nxtnum) :
        nxtnum=n1+n2
        l.append(nxtnum)
        n1=n2
        n2=nxtnum
    if(n  in l) :
        print("ISFIBO")
    else :
        print("ISNOTFIBO")
    t-=1