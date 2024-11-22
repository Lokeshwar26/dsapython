class animal:
    def speak(self):
        print("animal speaks")
class dog:
    def speak(self):
        print("dog barks")
class cat:
    def speak(self):
        print("cats meows")
    
def animal_sound(animal):
    animal.speak()

dog=dog()
cat=cat()
animal_sound(dog)
animal_sound(cat)