class Animal:
    def sound(self):
        print("this is sound")

class Dog(Animal):
    def sound(self):
        print("this is bow bow")
d = Animal()
d.sound()
