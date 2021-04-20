class Node:
  def __init__(self, data= None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def InBetween(self, middle, newdata):
    if middle is None:
      print("The node you are looking for is not present")
      return
    NewNode = Node(newdata)
    NewNode.next = middle.next
    middle.next = NewNode

  def listprint(self):
    printval = self.head
    while printval is not None:
      print(printval.data)
      printval= printval.next
list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.head.next= e2
e2.next = e3

list.InBetween(list.head.next,"Fri")

list.listprint()