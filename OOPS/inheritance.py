class Animal:
  location ="Australia"
  def __init__(self,name):
    self.name=name
  def speak(self):
    print("Speaking Now ...")
    
class Dog(Animal):
  def speak(self):
    super().speak()
    print("Woof!")

class Cat(Animal):
  def speak(self):
    super().speak()
    print("Meow!")

class Cow(Animal):
  def speak(self):
    super().speak()
    print("Moo!")


# a=Animal("Dog")
# a.speak()

# d=Dog("Bruno")
# d.speak()
# print(d.location)

c = Cat("Tom")
c.speak()
print(c.location)