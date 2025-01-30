def digitalroot(n) :
    sum=0
    while(n>=0) :
        sum+=n%10
        n=n//10
        if(sum>9 and n==0) :
            n=sum
            sum=0
        elif(n==0) :
            return sum
n=int(input("enter the number :"))
digitalroot=digitalroot(n)
print("the digital root of this number is ",digitalroot)

