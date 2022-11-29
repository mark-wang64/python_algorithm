class Listnode:
    def __init__(self, value): # initial elemant set-up
        self.data = value
        self.next = None
class LinkedList:
  
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
        
firstLinked = LinkedList()
firstLinked.head = Listnode(8)
second = Listnode(3)
third = Listnode(35)

firstLinked.head.next = second  # Link first node with second
second.next = third  # Link second node with the third node
  
firstLinked.printList()
