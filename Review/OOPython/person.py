class Person:
  numberOfPeople = 0 #this is defined for the whole class,same in all instances
  
  def __init__(self, name):
    self.name = name

p1 = Person("harry")
print(p1.numberOfPeople)
print(Person.numberOfPeople)