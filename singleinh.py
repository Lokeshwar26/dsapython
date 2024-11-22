class parent:
    def func1(self):
        print("This is a parent class")
class child(parent):
    def func2(self):
        print("this is a child class")

obj=child()
obj.func1()
obj.func2()