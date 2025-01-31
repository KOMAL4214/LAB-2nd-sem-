print("program of utopian tree")
t=int(input("enter the number of testcase :"))
while(t>0) :
    i=int(input("enter the number of cycles :"))
    height=1
    k=1
    def monsoon(height):
        height*=2
        return height
    def summer(height):
        height+=1
        return height
    while(k<=i) :
        if(k%2!=0) :
            height=monsoon(height)
        else :
            height=summer(height)
        k+=1
    print("the height of the sapling after ",i,"cycles is ",height,"meters")
    t-=1
