#Task 2
#Introducing head, insert and other functions in a linkedlist

#LinkedListNode is a class solely for the next value and the data
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
        
class LinkedList:

    def __init__(self, head=None):
        self.head=head
    
    def insert(self, data):
        node=LinkedListNode(data)
        if not self.head:
            self.head=node
            return
        CurrNode=self.head
        while CurrNode:
            if CurrNode.next is None:
                CurrNode.next=node
                break
            CurrNode=CurrNode.next
    def PrintLinkedList(self):
        CurrNode=self.head
        while CurrNode:
            print(CurrNode.data, end=" --> ")
            CurrNode=CurrNode.next
        print("None")

#Creating an object ll from the linkedlist class
ll=LinkedList()
ll.insert("5")
ll.PrintLinkedList()
ll.insert("10")
ll.PrintLinkedList()
ll.insert("15")
ll.PrintLinkedList()
