# class node:
#   def _init_ (self, data = None):
#     self.data = data
#     self.next = None

# class linked_list:
#   def __init__(self):
#     self.head = node() #user cant access this, simply points to the head nodes
#   def append(self, data):
#     new_node = node(data)
#     currrent = self.head
#     while(currrent.next != None):
#       current = currrent.next
#     current.next = new_node
#   def length(self):
#     current = self.head
#     total = 0
#     while (current.next != None):
#       total += 1
#       current = current.next
#     return total
#   def display(self):
#     elems = []
#     current_node = self.head
#     while current_node.next != None:
#       current_node= current_node.next
#       elems.append(current_node.data)
#     print(elems)

# myList = linked_list()
# myList.display()