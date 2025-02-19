class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area of this rectangle is :",self.length*self.breadth)
    def perimeter(self):
        print("perimeter of this rectangle is :",2*(self.length+self.breadth))
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of this circle is :",(3.14)*(self.radius**2))
    def perimeter(self):
        print("perimeter/circumference of this circle is :",2*3.14*self.radius)
print("choose:1->rectangle")
print("choose:2->circle")
global ch
ch=int(input("enter the choice :"))
if(ch==1):
    length=int(input("enter the length of rectangle :"))
    breadth=int(input("enter the breadth of rectangle :"))
    class shape(rectangle):
        def __init__(self,length,breadth):
            rectangle.__init__(self,length,breadth)
    r=shape(length,breadth)
    r.area()
    r.perimeter()
elif(ch==2):
    radius=int(input("enter the radius of circle :"))
    class shape(circle):
        def __init__(self,radius):
            circle.__init__(self,radius)
    c=shape(radius)
    c.area()
    c.perimeter()