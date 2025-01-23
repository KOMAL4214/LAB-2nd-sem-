proprice=dict()
n=int(input("enter the number of products"))
for i in range (0,n) :
    proname=input("enter the product name :")
    proprice[proname]=float(input("enter the cost of this product :"))
i=input("enter YOUR product name :")
if(i in proprice) :
    print("the price of this product is : ",proprice[i])
else :
    print("the product is not present")