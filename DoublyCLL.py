class Node:
    __slots__ = '_element', '_next', '_prev'
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev
class DoublyCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def isempty(self):
        return self.size==0
    def addlst(self, e):
        newest = Node(e, None, None)
        if self.isempty():
            newest._next = newest
            newest._prev = newest
            self.head = newest
            self.tail = newest
        else:
            newest._prev = self.tail
            self.tail._next = newest
            newest._next = self.head
            self.tail = newest
        self.size+=1
    def addfst(self, e):
        newest = Node(e, None, None)
        if self.isempty():
            newest._next = newest
            newest._prev = newest
            self.head = newest
            self.tail = newest
        else:
            newest._next = self.head
            newest._prev = self.tail
            self.tail._next = newest
            self.head._prev = newest
            self.head = newest
        self.size+=1
    def addany(self, e, position):
        newest = Node(e, None, None)
        if self.isempty():
            newest._next = newest
            newest._prev = newest
            self.head = newest
            self.tail = newest
        else:
            p = self.head
            i = 1
            while i<(position-1):
                p = p._next
                i+=1
            newest._next = p._next
            newest._prev = p
            p._next = newest
        self.size+=1
    def rmlst(self):
        if self.isempty():
            print("list is empty")
            return
        else:
            e = self.tail._element
            self.tail._prev._next = self.head
            self.tail = self.tail._prev
            print(e, "deleted from last")
        self.size-=1
    def rmfst(self):
        if self.isempty():
            print("list is empty")
            return
        else:
            e = self.head._element
            self.tail._next = self.head._next
            self.head = self.head._next
            self.head._prev = self.tail
            print(e, "deleted from first")
        self.size-=1
    def rmany(self, position):
        if position>len(self):
            print("Enter position value less than or equal to ", position)
        elif self.isempty():
            print("list empty")
            return
        else:
            p = self.head
            i = 1
            while i<(position-1):
                p = p._next
                i+=1
            e = p._next._element
            p._next = p._next._next
            p._next._next._prev = p
            print(e, " is deleted from position ",  position)
        self.size-=1

    def display(self):
        p = self.head
        while p:
            if p._next == self.head:
                print(p._element)
                break
            else:
                print(p._element, end="<-->")
            p = p._next
dcll = DoublyCLL()
dcll.addlst(4)
dcll.addlst(6)
dcll.addlst(8)
dcll.addlst(24)
dcll.addfst(100)
dcll.addany(880, 4)
dcll.rmlst()
dcll.rmfst()
dcll.rmany(3)
dcll.display()