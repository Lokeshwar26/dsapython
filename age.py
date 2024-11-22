class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun2(self):
        return self.age>=18
        
per1=person("loki",20)
per2=person("sai",25)
per3=person("nitin",15)

print(f"{per1.name} is an adult? {per1.fun2()}")
print(f"{per2.name} is an adult? {per2.fun2()}")
print(f"{per3.name} is an adult? {per3.fun2()}")