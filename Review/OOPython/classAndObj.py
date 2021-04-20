#creating blueprint for any object of type dog
class Dog:

  def __init__(self, name, age):
    self.name = name #attribute of dog object has been created
    self.age = age
      # init is called whenever you create an instance of the class
  
  def get_name(self):
    return self.name

  def get_age(self):
    return self.age 
  
  def set_age(self,age):
    self.age = age


d= Dog("Tim", 34)
d.set_age(54)
print(d.get_age())