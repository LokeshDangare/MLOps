# Base Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):

    def speak(self):
        print(f"{self.name} barks.")

# Create an instance of Animal
animal = Animal("Generic Animal")
animal.speak()

# Create an instance of Dog
dog = Dog("Mercy")
dog.speak()