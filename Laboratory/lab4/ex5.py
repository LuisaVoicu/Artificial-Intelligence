import math

class GeometricForm():

    def getArea(self):
        pass
    def getPerimeter(self):
        pass

class Circle(GeometricForm):
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return math.pi*self.radius
    def getPerimeter(self):
        return 2*math.pi*self.radius

class Rectangle(GeometricForm):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def getArea(self):
        return self.length*self.width
    def getPerimeter(self):
        return 2*(self.length+self.width)

circle1 = Circle(2)
circle2 = Circle(1)
rectangle = Rectangle(1,2)

listGeometricForms = [circle1, circle2, rectangle]

for form in listGeometricForms:
    area = form.getArea()
    perimeter = form.getPerimeter()
    print("area=", area, " -- perimeter=", perimeter)