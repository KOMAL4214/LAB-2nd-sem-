import random
mcount=0
count=0
list=[]
for i in range (0,100) :
    list.insert(i,round(random.random()))
print(list)
for i in range(0,100) :
    if(list[i]==0) :
        count+=1
    else :
        if(mcount<=count) :
            mcount=count
        count=0
print("the number of consecutive zeros are :",mcount)
