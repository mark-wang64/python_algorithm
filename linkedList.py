class listNode:
    def __init__(self, value): # initial elemant set-up
        self.data = value
        self.next = None
class linkedList:
  
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def push(self, newData): # Add in the head
        newNode = listNode(newData)
        newNode.next = self.head
        self.head = new_node
    def insert(self, pervNode, newData)
        if prevNode is None:
            print("the previous node must be Linkedlist")
            return
        newNode = listNode(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
#    def delete(self, key)
#        temp = self.head
#        if temp == 0:
#            print("no value")
#        while temp:
            
        
firstLinked = LinkedList()
firstLinked.head = Listnode(8)
second = Listnode(3)
third = Listnode(35)

firstLinked.head.next = second  # Link first node with second
second.next = third  # Link second node with the third node
  
firstLinked.printList()
