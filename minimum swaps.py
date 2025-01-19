print("program for minimum swaps")
heights=[]
dup=[]
n=int(input("enter the number of persons :"))
k=0
for i in range (0,n) :
    heights.append(int(input("enter the height of the person")))
for i in range (0,n) :
    if (heights[i]-1!=i) :
        l=heights[i]
        heights[i],heights[l-1]=heights[l-1],heights[i]
        k+=1
for i in range (0,n) :
    if (heights[i]-1!=i) :
        l=heights[i]
        heights[i],heights[l-1]=heights[l-1],heights[i]
        k+=1
print(heights)
print(k)
