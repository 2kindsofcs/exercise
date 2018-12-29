# single linked list 예제

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def newnodehead(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def newnodeend(self, newdata):
        newnode = Node(newdata)
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = newnode          
    
    def newnodemiddle(self, middlenode, newdata):
        newnode = Node(newdata)
        newnode.next = middlenode.next
        middlenode.next = newnode

def delxthnode(head, x): #head와 지우고자 하는 노드의 차례를 받고 지운 노드의 data를 리턴
    if x == 1:
        data = head.data
        head = head.next
        return data
    countnum = 1
    element = head
    prev = None
    while countnum < x:
        prev = element
        element = element.next
        countnum += 1
    prev.next = element.next
    return element.data    


list1 = SLinkedlist()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.newnodehead("Sun")
list1.newnodeend("Thu")
list1.newnodemiddle(e2, "히히 못가")

list1.printlist()
print(delxthnode(list1.head, 4))

    
