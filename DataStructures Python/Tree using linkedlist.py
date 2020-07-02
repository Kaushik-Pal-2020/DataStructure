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
        for i in range(0, len(arr), 2):
            l = arr[i]
            r = arr[i+1]
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

    def func_height(self, root):
        if root:
            x = self.func_leaf(root.leftchild)
            y = self.func_leaf(root.rightchild)
            if x > y:
                return x+1
            else:
                return y+1
        else:
            return 0

    def func_count(self, root):
        if root:
            x = self.func_leaf(root.leftchild)
            y = self.func_leaf(root.rightchild)
            return x+y+1
        else:
            return 0

    def func_leaf(self, root):
        if root:
            x = self.func_leaf(root.leftchild)
            y = self.func_leaf(root.rightchild)
            if root.leftchild == None and root.rightchild == None:
                return x+y+1
            else:
                return x+y
        else:
            return 0

    def func_degree_two_nodes(self, root):
        if root:
            x = self.func_leaf(root.leftchild)
            y = self.func_leaf(root.rightchild)
            if root.leftchild and root.rightchild:
                return x+y+1
            else:
                return x+y
        else:
            return 0


if __name__ == "__main__":
    t = Tree("a")
    t.insertArray(["b", "c", "d", "e", "f", "g"])
    print("printing Preorder\n")
    t.preorder(t.root)
    print()

    print("printing Inorder\n")
    t.inorder(t.root)
    print()

    print("printing Postorder\n")
    t.postorder(t.root)
    print('\n')
    print(f"total leaf nodes = {t.func_leaf(t.root)}")
    print(f"total nodes = {t.func_count(t.root)}")
    print(f"height  = {t.func_height(t.root)}")
    print(f"total degree two nodes = {t.func_degree_two_nodes(t.root)}")
