class Node():
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinaryTree():
    def __init__(self):
        self.root = None
        self.count = 0
        
    def insertI(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            tail = self.root
            forward = self.root
            while forward :
                tail = forward
                if value > forward.data :
                    forward = forward.rightchild
                elif value < forward.data :
                    forward = forward.leftchild
                elif value == forward.data:
                    return

            if value < tail.data:
                tail.leftchild = Node(value)
            else:
                tail.rightchild = Node(value)

    def insertR(self, root, val):
        if root == None:
            t = Node(val)
        elif root.data < val:
            root.rightchild = self.insertR(root.rightchild, val)
        elif root.data > val:
            root.leftchild = self.insertR(root.leftchild, val)
        return root

    def build(self, array):
        try:
            if len(array) < 1:
                raise
            for values in array:
                self.insertI(values)
            
        except:
            print("Build function expects list or tuple of values and None type object passed")
        
    def preorder(self, root):
        if root:
            print(f"{root.data} -> ",end='')
            self.preorder(root.leftchild)
            self.preorder(root.rightchild)
    
    def inorder(self, root):
        if root:
            self.inorder(root.leftchild)
            print(f"{root.data} -> ",end='')
            self.inorder(root.rightchild)

    def postorder(self, root):
        if root:
            self.postorder(root.leftchild)
            self.postorder(root.rightchild)
            print(f"{root.data} -> ",end='')

    def search(self, key):
        try:
            if self.root == None:
                raise
            forward = self.root
            while forward:
                if key == forward.data:
                    return True
                elif key > forward.data:
                    forward = forward.rightchild
                elif key < forward.data:
                    forward = forward.leftchild
            return False
        except:
            print("Root is None")

    def count(self, root):
        if root:
            x = self.count(root.leftchild)
            y = self.count(root.rightchild)
            return x+y+1
        else:
            return 0
    
    def sum(self, root):
        tot = 0
        if root:
            x = self.sum(root.leftchild)
            y = self.sum(root.rightchild)
            return x+y+root.data
        else:
            return 0

    def leafNodes(self, root):
        if root :
            x = self.leafNodes(root.leftchild)
            y = self.leafNodes(root.rightchild)
            if not root.leftchild and not root.leftchild:
                return x+y+1
            else:
                return x+y
        else:
            return 0

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insertI(20)
    bt.insertI(10)
    bt.insertI(30)
    # bt.insertR(bt.root, 45)
    # bt.insertR(bt.root, 5)
    # bt.insertR(bt.root, 15)
    bt.insertI(45)
    bt.insertI(5)
    bt.insertI(15)

    print(f"\nPreoder of the binary tree :")
    bt.preorder(bt.root)

    print(f"\nInoder of the binary tree :")
    bt.inorder(bt.root)
    
    print(f"\nPostoder of the binary tree :")
    bt.postorder(bt.root)
    s = [x for x in range (0,100,10)]
    bt.build(s)

    print(f"\nInoder of the binary tree :")
    bt.inorder(bt.root)
    print()

    print(bt.search(80))
    print(bt.search(-5))
    bt2 = BinaryTree()
    bt2.insertI(20)
    bt2.insertI(10)
    bt2.insertI(30)
    print(bt2.leafNodes(bt2.root))
