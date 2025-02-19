class convertor:
    def __init__(self,length,units):
        if(units=="inches"):
            self.k=length*0.0254
        if(units=="feet"):
            self.k=length*0.3048
        if(units=="yards"):
            self.k=length*0.9144
        if(units=="miles"):
            self.k=length*1609.344
        if(units=="kilometers"):
            self.k=length*1000
        if(units=="meters"):
            self.k=length
        if(units=="centimeters"):
            self.k=length*0.01
        if(units=="millimeters"):
            self.k=length*0.001
    def feet(self):
        print(self.k*3.28084)
    def inches(self):
        print(self.k*39.37008)
    def yards(self):
        print(self.k*1.093613)
    def miles(self):
        print(self.k*0.000621)
    def kilometers(self):
        print(self.k*0.001)
    def meters(self):
        print(self.k)
    def centimeters(self):
        print(self.k*100)
    def millimeters(self):
        print(self.k*1000)
c=convertor(9,"inches")
c.feet()        