class rectangle:
    def __init__(self,length,breadth):
        self.l = length
        self.b = breadth

    def area(self):
        return(self.l*self.b)

l = int(input("Enter length :"))
b = int(input("Enter breadth :"))
r = rectangle(l,b)
print("Area of the rectangle :",r.area())