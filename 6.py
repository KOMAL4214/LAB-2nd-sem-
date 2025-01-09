print("reverse number")
num=int(input("enter the number :"))
k=0
while(num>0) :
    q=num%10
    k=k*10+q
    num=num//10
print("the reverse number is ",k)