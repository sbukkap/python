class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class Btree:
    def __init__(self):
        self.root=None
    def insert(self,node):
        if node.data == 3:
            self.root = node
            print('inserted')
        elif node.data == 1:
            self.root.left = node
            print('inserted')
        elif node.data == 4:
            self.root.right = node
            print('inserted')
        elif node.data == 2:
            self.root.right.left = node
            print('inserted')
    def recoverTree(self):
        stack = []
        swap = []
        first_time = 0
        while self.root!=None or len(stack)!=0:
            while self.root!=None:
                stack.append(self.root)
                self.root = self.root.left
            self.root = stack.pop()
            if first_time == 0:
                first_time = 1
            elif self.root.data < prev.data:
                swap.append([self.root,prev])
            prev = self.root
            self.root = self.root.right
        return swap
tree = Btree()
node1 = node(3)
tree.insert(node1)
node2 = node(1)
tree.insert(node2)
node3 = node(4)
tree.insert(node3)
node4 = node(2)
tree.insert(node4)
print(tree.recoverTree())
