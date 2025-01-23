i=int(input("enter the number of testcases : "))
while(i>0) :
    l=0
    n=int(input("enter the number : "))
    k=n
    while(n>0) :
        if(k%(n%10)==0) :
            l+=1
        n=n//10
    print("this number is divided by ",l," digits")
    i-=1