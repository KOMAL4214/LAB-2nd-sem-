t=int(input("enter number of testcases :"))
while(t>0):
    str=input("enter the string : ")
    operation=0
    k=1
    if(len(str)%2==0) :
        for i in str[(len(str)//2):]:
            while(i!=str[len(str)//2-k]) :
                j=ord(i)
                j-=1
                i=chr(j)
                operation+=1
            k+=1
    else :
        for i in str[((len(str)//2)+1):] :
            while(i!=str[(len(str)//2)-k]):
                j=ord(i)
                j-=1
                i=chr(j)
                operation+=1
            k+=1
    print(operation)
    t-=1