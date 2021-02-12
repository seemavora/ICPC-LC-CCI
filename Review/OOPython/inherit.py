# class Cat:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def speak(self):
#     print("meow")

# class Dog:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def speak(self):
#     print("Bark")

class Pet: 
  def __init__(self, name , age):
    self.name = name
    self.age = age
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
  def speak(self):
    print("meow")
  def show(self):
    print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
  def speak(self):
    print("Bark")


p = Pet("Buddy", 23)
p.show()
c = Cat("Ugle", 32, "Blue")
c.speak()
c.show()