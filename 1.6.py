print("program to find nearest point ")
points=[]
nearest_points=[]
p=[]
a=()
for i in range(0,4) :
    x=int(input("enter the x coordinate here :"))
    y=int(input("enter the y coordinate here :"))
    z=int(input("enter the z coordinate here :"))
    point=x,y,z
    points.append(point)
from math import sqrt as sq
l=0
j=0
for k in range (0,4) :
    if(k==1) :
        dis=sq((((points[k][0])-points[2][0])**2)+(((points[k][1])-points[2][1])**2)+(((points[k][2])-points[2][2])**2))
    else :
        dis=sq((((points[k][0])-points[1][0])**2)+(((points[k][1])-points[1][1])**2)+(((points[k][2])-points[1][2])**2))
    for i in range (0,4) :
        if(k!=i):
            l=sq((((points[k][0])-points[i][0])**2)+(((points[k][1])-points[i][1])**2)+(((points[k][2])-points[i][2])**2))
            if (l<=dis):
                dis=l
                a=points[i]
                p.append(a)
                if(len(p)>1) :
                    p.remove(p[0])
                j+=1
    nearest_points.append(p)
    p=[] 
    j=0 
    l=0
    dis=0            
print(nearest_points)