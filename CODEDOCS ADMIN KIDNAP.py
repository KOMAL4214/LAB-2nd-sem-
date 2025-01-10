t=int(input("enter the number of testcases :"))
while (t>0) :
    n=int(input("enter the number of boxes : "))
    x=int(input("enter the box number where the gold coin should be placed : "))
    box=[ 0 if(i==x-1) else 1  for i in range(0,n)]
    s=int(input("enter the number of swaps : "))
    while(s>0) :
        a=int(input("enter the number of box to be swapped :"))
        b=int(input("enter the number of other box to be swapped :"))
        k=box[a-1]
        box[a-1]=box[b-1]
        box[b-1]=k
        s-=1
    i=0
    while (i<n) :
        if box[i]==0:
            print("THE GOLD COIN IS PRESENT IN THE BOX OF NUMBER : ",i+1)
            break
        i+=1
    t-=1
