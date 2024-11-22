class rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area(self):
        return self.len*self.wid
    def peri(self):
        return 2*(self.len*self.wid)
    
rect1=rectangle(10,15)
rect2=rectangle(5,7)

print(f"rectangle 1- length:{rect1.len},width:{rect1.wid}")
print(f"area of rectangle 1 is:{rect1.area()}")
print(f"perimeter of the rectangle 1 is:{rect1.peri()}")

print(f"rectangle 2- length:{rect2.len},width:{rect2.wid}")
print(f"area of rectangle 2 is:{rect2.area()}")
print(f"perimeter of the rectangle 2 is:{rect2.peri()}")