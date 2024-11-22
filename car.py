class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_details(self):
        print(self.brand, "is launched in",self.year,"the model is",self.model)
car1=car("maruthi","swift",2005)
car2=car("toyota","fortuner",2015)
car3=car("isuzu","d max",2007)

car1.display_details()
car2.display_details()
car3.display_details()