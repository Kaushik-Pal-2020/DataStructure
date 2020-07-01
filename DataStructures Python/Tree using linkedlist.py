class Node():
    def __init__(self, value):
        self.value = value
        self.leftchild = None 
        self.rightchild = None

class Tree():
    def __init__(self, value):
        self.root = Node(value)
        self.height = -1
        self.values = [value]
        self.element = 0
        self.links = [self.root]

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
        return self.element

    def __getitem__(self, value):
        return self.values[value]

    def __contains__(self, value):
        for v in self.values:
            if v == value:
                return True
        return False

    def __iter__(self):
        return self.root

    def insertChild(self, leftchild_value=None, rightchild_value=None):
        flag = 0
        temp_root = self.links.pop(0)
        if leftchild_value:
            new_node = Node(leftchild_value)
            temp_root.leftchild = new_node
            self.values.append(leftchild_value)
            self.links.append(new_node)
            self.element += 1
            flag = 1
        if rightchild_value:
            new_node = Node(rightchild_value)
            temp_root.rightchild = new_node
            self.values.append(rightchild_value)
            self.links.append(new_node)
            self.element += 1
            flag = 1
        
        if flag == 1:
            self.height += 1

    def insertArray(self, arr):
        for i in range(2, len(arr), 2):
            l = arr[i - 2]
            r = arr[i - 1]
            self.insertChild(l, r)

        if len(arr) % 2 != 0:
            self.insertChild(arr[len(arr) - 1])

    def preorder(self, root):
        if root:
            print(root.value, end=" -> ")
            self.preorder(root.leftchild)
            self.preorder(root.rightchild)

    def postorder(self, root):
        if root:
            self.postorder(root.leftchild)
            self.postorder(root.rightchild)
            print(root.value, end=" -> ")

    def inorder(self, root):
        if root:
            self.inorder(root.leftchild)
            print(root.value, end=" -> ")
            self.inorder(root.rightchild)

if __name__ == "__main__":
    t = Tree("a")
    t.insertArray(["b", "c", "d", "e", "f", "g", "h"])
    print("printing Preorder\n")
    t.preorder(t.root)
    print()

    print("printing Inorder\n")
    t.inorder(t.root)
    print()

    print("printing Postorder\n")
    t.postorder(t.root)
