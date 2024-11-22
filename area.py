import math
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    
circle=circle(5)
square=square(8)

print(f"area of the circle of radius{circle.radius} is {circle.area():.2f}")
print(f"area of the square is {square.side} is {square.area()}")