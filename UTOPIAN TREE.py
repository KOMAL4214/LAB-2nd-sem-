print("program of utopian tree")
t=int(input("enter the number of testcase :"))
while(t>0) :
    i=int(input("enter the number of cycles :"))
    height=1
    k=1
    while(k<=i) :
        if(k%2==0) :
            height+=1
        else :
            height*=2
        k+=1
    print("the height of the sapling after ",i,"cycles is ",height,"meters")
    t-=1