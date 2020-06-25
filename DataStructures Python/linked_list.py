class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head:
            p = Node(data)
            q = self.head
            while q.next:
                q = q.next
            q.next = p
        else:
            p = Node(data)
            self.head = p
        
    def display(self):
        q = self.head
        while q :
            print(f"{q.data} -> ",end='')
            q = q.next
        print('None')

    def insert(self,pos,data):
        try:
            p = Node(data)
            if pos==0:
                p.next = self.head.next
                self.head = p

            else:
                q = self.head
                i = 1
                while i<pos:
                    q = q.next
                    i += 1
                p.next = q.next
                q.next = p
        except :
            print("Invalid Index")

    @property        
    def length(self):
        q = self.head
        count = 0
        while q :
            count += 1
            q = q.next
        return count

    def index(self,pos):
        ''' hello this is a function
        '''
        if pos>=self.length:
            print("Invalid Index for getting an element")
            return None
        else:
            q = self.head
            i = 0
            while i<pos:
                i +=1
                q = q.next

            return q.data

    def pop(self,pos = "Base"):
        if pos=='Base':
            q = self.head
            while q.next.next:
                q = q.next
            p = q.next
            q.next = None
            value = p.data
            del p
            return value

        else:
            if pos>=self.length and pos<0:
                print("Invalid Index for poping an element")
                return 

            else:
                if pos ==0 :
                    q = self.head
                    value = q.data
                    self.head = self.head.next
                    del q
                    return value
                else:
                    q = self.head
                    i = 1
                    while i<pos and q.next:
                        q = q.next
                        i += 1
                    p = q.next
                    q.next = p.next
                    p.next=None
                    value = p.data
                    del p
                    return value
    @property
    def sum(self):
        count = 0
        q = self.head
        while q.next:
            count += int(q.data)
            q = q.next
        return count

    @property
    def min(self):
        q = self.head
        val = int(q.data)
        while q.next:
            if val >= int(q.data):
                val = int(q.data)
            q = q.next
        return val

    @property
    def max(self):
        q = self.head
        val = int(q.data)
        while q.next:
            if val <= int(q.data):
                val = int(q.data)
            q = q.next
        return val

    def isSorted(self):
        q = self.head
        val = int(q.data)
        while q.next:
            if val > int(q.data):
                return False
            q = q.next
        return True

    def append_from_list(self,arr):
        for value in arr:
            self.append(value)

    def sorted_insertion(self,data):
        q = self.head
        if data<int(q.data):
            p = Node(data)
            p.next = q
            self.head = p
        else:
            p = Node(data)
            t = self.head
            q = t.next
            while int(q.data) <= data and q.next:
                t = q
                q = q.next
            if q.next == None:
                q.next = p
            else:
                t.next = p
                p.next = q

    def remove_duplicate(self):
        try:
            p = self.head
            q = p.next
            count = 0
            while q:
                if int(p.data)!=int(q.data):
                    p = q
                    q = q.next
                else:
                    p.next = q.next
                    del q
                    q = p.next
                    count += 1

            return count
        except :
            print("Only one element in the linked list")

    def reverse(self):
        forward = self.head
        current = None
        tail = None
        while forward:
            tail = current
            current = forward
            forward = forward.next
            current.next = tail
        self.head = current

    def checkLoop(self):
        tail = self.head
        current = None
        while tail!=current and tail:
            current = tail
            tail = tail.next
        if tail==current:
            return True
        else:
            return False

    def concat(self,another):
        q = self.head
        while q.next:
            q = q.next
        q.next = another.head


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append_from_list([1,2,3,4,5,6,7,8,9,10])
    l1.display()
    print(l1.sum)
    print(l1.min)
    print(l1.isSorted())
    l1.sorted_insertion(0)
    l1.sorted_insertion(6.5)
    l1.sorted_insertion(11)
    l1.display()
    l1.reverse()
    l1.display()

    l1.pop(5)
    l1.display()
    print(l1.checkLoop())
    l2 = LinkedList()
    l2.append_from_list([15,16,17,18])
    l1.concat(l2)
    l1.display()
    l2.concat(l1)
    l2.display()