class calculator:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return self.num1+self.num2
    
calci=calculator()
a1=calci.add(4,5)

print(f"the sum of {calci.num1} and {calci.num2} is {a1}")
a2=calci.add(9,8)
print(f"the sum of {calci.num1} and {calci.num2} is {a2}")