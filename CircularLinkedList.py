class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next
class CircularLinkedList:
    def __init__(self):
        print("cll called")
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def isempty(self):
        return self.size==0
#Functions for inserting elements inside Circular Linked List
    def addlast(self, e):
        newest = Node(e, None)
        if self.isempty():
            newest._next = newest
            self.head = newest
            self.tail = newest
        else:
            self.tail._next = newest
            newest._next = self.head
        self.tail = newest
        self.size+=1
    def addfirst(self, e):
        newest = Node(e, None)
        if self.isempty():
            newest._next = newest
            self.head = newest
            self.tail = newest
        else:
            newest._next = self.head
            self.head = newest
            self.tail._next = newest
        self.size+=1
    def addany(self, e, position):
        newest = Node(e, None)
        if self.isempty():
            newest._next = newest
            self.head = newest
            self.tail = newest
        else:
            p = self.head
            i = 1
            while i<(position-1):
                p = p._next
                i+=1
            newest._next = p._next
            p._next = newest
        self.size+=1
    def rmfirst(self):
        if self.isempty():
            print("List is empty")
            return
        else:
            self.head = self.head._next
            self.tail._next = self.head
        self.size-=1
    def rmlst(self):
        if self.isempty():
            print("List is empty")
            return
        else:
            p = self.head
            i = 1
            while i<(len(self)-1):
                p = p._next
                i+=1
            p._next = self.head
            self.tail = p
            self.size-=1
    def rmany(self, position):
        if position> len(self):
            print("please enter position number below ", self.size)
        elif self.isempty():
            print("List is empty")
            return
        else:
            p = self.head
            i = 1
            while i<(position-1):
                p = p._next
                i+=1
            e = p._next._element
            p._next = p._next._next
            self.size-=1
            print(e, "is deleted from position", position)
    def display(self):
        p = self.head
        while p:
            if p._next == self.head:
                print(p._element)
                break

            else:
                print(p._element, end = "-->")
            p = p._next






Cll = CircularLinkedList()
Cll.addlast(4)
Cll.addlast(6)
Cll.addlast(8)
Cll.addlast(5)
Cll.addfirst(67)
Cll.addany(15,-1)
Cll.rmfirst()
Cll.display()
#Cll.rmlst()
Cll.rmany(15)
Cll.display()
