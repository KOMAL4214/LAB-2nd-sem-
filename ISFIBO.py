t=int(input("enter the number of testcases :"))
while(t>0) :
    n=int(input("enter the required number :"))
    l=[]
    def isfibo(n):
        n1=0
        n2=1
        l.append(n1)
        l.append(n2)
        nxtnum=n1+n2
        while(nxtnum<=n):
            nxtnum=n1+n2
            l.append(nxtnum)
            n1=n2
            n2=nxtnum
        if(n in l):
            print("isfibo")
        else:
            print("isnotfibo")
    isfibo(n)
    t-=1
