class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def display(self):
    print(f"Name:{self.name},Species:{self.species}")

class Dog(Animal):
  def work(self): 
    print(f"{self.name} is barking")
dog1 = Dog("Buddy","Canine")
dog1.display()
dog1.work()
