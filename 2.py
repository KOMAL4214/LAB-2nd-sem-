print("factorial of a number")
num=int(input("number ="))
fact=1
while(num>0):
    fact*=num
    num=num-1
print("factorial of the number is ",fact)