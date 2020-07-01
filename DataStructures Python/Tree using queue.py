class Tree:
    def __init__(self, root_value):
        self.root = root_value
        self.lchild = None
        self.rchild = None
        self.queue = [self]
        self.height = -1
        self.values = [self.root]

    @property
    def getHeight(self):
        return self.height

    @property
    def getLevel(self):
        return self.height + 1

    def __str__(self):
        return ", ".join(self.values)

    def __eq__(self, value):
        if value.values == self.values:
            return True
        else:
            return False

    def __len__(self):
        return len(self.values)

    def __getitem__(self, value):
        return self.values[value]

    def __contains__(self, value):
        for v in self.values:
            if v == value:
                return True
        return False

    def __iter__(self):
        return self.values

    def insertChild(self, lchild_value=None, rchild_value=None):
        try:
            temp_root = self.queue.pop(0)
            flag = 0
            if lchild_value:
                childLeft = Tree(lchild_value)
                temp_root.lchild = childLeft
                self.queue.append(childLeft)
                self.values.append(lchild_value)
                flag = 1

            if rchild_value:
                childRight = Tree(rchild_value)
                temp_root.rchild = childRight
                self.queue.append(childRight)
                self.values.append(rchild_value)
                flag = 1

            if flag == 1:
                self.height += 1
        except:
            print("Queue is empty")

    def insertArray(self, arr):
        for i in range(2, len(arr), 2):
            l = arr[i - 2]
            r = arr[i - 1]
            self.insertChild(l, r)

        if len(arr) % 2 != 0:
            self.insertChild(arr[len(arr) - 1])

    def preorder(self, new_self):
        if new_self:
            print(new_self.root, end=" -> ")
            new_self.preorder(new_self.lchild)
            new_self.preorder(new_self.rchild)

    def postorder(self, new_self):
        if new_self:
            new_self.postorder(new_self.lchild)
            new_self.postorder(new_self.rchild)
            print(new_self.root, end=" -> ")

    def inorder(self, new_self):
        if new_self:
            new_self.inorder(new_self.lchild)
            print(new_self.root, end=" -> ")
            new_self.inorder(new_self.rchild)


if __name__ == "__main__":
    t = Tree("a")
    t.insertArray(["b", "c", "d", "e", "f", "g", "h"])
    print("printing Preorder\n")
    t.preorder(t)
    print()

    print("printing Inorder\n")
    t.inorder(t)
    print()

    print("printing Postorder\n")
    t.postorder(t)
