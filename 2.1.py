word=input("enter the word :")
l=list(word)
for i in range(0,len(word)) :
    if(i%2==1) :
        l[i]=l[i].upper()
    l[0]+=l[i]
print(l[0][1:len(l[0])])
        
    
