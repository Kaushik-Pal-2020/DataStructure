class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.count = 0
        self.i = 0

    def print_all(self, reverse=False):
        print("=" * 50)
        q = self.head
        if reverse == False:
            print(f"Displaying elements of Doubly Linkedlist Forward")
            while q:
                print(f"{q.data} -> ", end="")
                q = q.next
        else:
            print(f"Displaying elements of Doubly Linkedlist Backward")
            while q.next:
                q = q.next
            while q != self.head:
                print(f"{q.data} -> ", end="")
                q = q.prev
        print()
        print("=" * 50)

    def push(self, value):
        if self.head == None:
            p = Node(value)
            self.head = p
        else:
            p = Node(value)
            q = self.head
            while q.next:
                q = q.next
            q.next = p
            p.prev = q
            self.count += 1

    def __contains__(self, parameter):
        q = self.head
        while q:
            if q.data == parameter:
                return True
            q = q.next
        return False

    def __eq__(self, value):
        try:
            q = self.head
            p = value.head
            while q and p:
                if q.data != p.data:
                    return False
                else:
                    p = p.next
                    q = q.next
            return True
        except:
            print("Invalid equal Operation")

    def __getitem__(self, position):
        if position > self.count:
            raise IndexError
        else:
            i = 0
            q = self.head
            while i < position and q:
                q = q.next
                i += 1
            return q.data

    def __reversed__(self):
        try:
            q = self.head
            while q:
                q.next, q.prev = q.prev, q.next
                q = q.prev
                if q.next == None:
                    self.head = q
            return True
        except:
            return False

    def __len__(self):
        return self.count + 1

    def __str__(self):
        return f"Total nodes in this LinkedList = {self.count+1}"

    def __iter__(self):
        return self.head

    def __next__(self):
        q = self.head
        if q == None and self.i > self.count:
            raise StopIteration

        else:
            value = self.__getitem__(self.i)
            self.i += 1
            return value

    def pop(self, position="end"):
        if position == "end":
            position = int(self.count)
        if position < 0 and position > self.count:
            print("Invalid Index")
            return -90
        else:
            if self.head.data != None:
                if position == 0:
                    q = self.head
                    self.head = q.next
                    value = q.data
                    q.next = None
                    self.head.prev = None
                    del q
                    return value
                else:
                    q = self.head
                    p = q
                    i = 0
                    while q.next and i < position:
                        p = q
                        q = q.next
                        i += 1
                    value = q.data
                    q.data = None
                    p.next = q.next
                    return value
            else:
                print("Linked List is empty")


if __name__ == "__main__":
    d = DoublyLinkedlist()
    d.push(1)
    d.push(2)
    d.push(3)
    d.push(6)
    d.push(10)
    d.print_all(reverse=True)

    # print(d.pop())
    # d.print_all()
    # print(d.pop(2))
    # d.print_all()
    # print(d.pop(0))
    # d.print_all()

    print(d[3])
    reversed(d)
    d.print_all()
    print(d.__iter__())
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
    print(next(d))
