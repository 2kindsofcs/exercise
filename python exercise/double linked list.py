# single linked list 예제를 따라해본 뒤 응용해서 만들어 본 double linked list

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail

    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def append(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            self.tail = newnode 
        else:
            newnode.prev = self.tail
            newnode.next = None
            self.tail.next = newnode
            self.tail = newnode

#   def deletenode(self, delnode): 노드 삭제 추가해야함
        


list1 = DLinkedlist()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.newnodehead("Sun")
list1.newnodeend("Thu")
list1.newnodemiddle(e2, "히히 못가")

list1.printlist()