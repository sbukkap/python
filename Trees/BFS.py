#Creating a tree first using my code and then traversing it in a BFS fashion
class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root =None
    def insert(self,node):
        if not self.root:
            self.root = node
        else:
            temp=self.root
            while True:
                if node.val>=temp.val:
                    if temp.right is None:
                        break
                    temp=temp.right
                else:
                    if temp.left is None:
                        break
                    temp=temp.left
            if node.val>=temp.val:
                temp.right=node
            else:
                temp.left=node
            print('inserted')
    def BFS(self):
        #without usinf for loop
        """
        queue = [self.root]
        while len(queue) != 0:
            x=queue.pop(0)
            print(x.val)
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        print('traversal complete')
        """
        #usin for loop
        queue = [self.root]
        j=1
        while len(queue) != 0:

            s = len(queue)
            print(f'level {j}')
            for i in range(s):
                x = queue.pop(0)
                print(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            j+=1
        print('traversal complete')
tree = Tree()
node1 = node(9)
tree.insert(node1)
node2=node(5)
tree.insert(node2)
node3=node(15)
tree.insert(node3)
node4=node(6)
tree.insert(node4)
node5=node(4)
tree.insert(node5)
node6=node(16)
tree.insert(node6)
node7=node(10)
tree.insert(node7)
node8=node(13)
tree.insert(node8)
node9=node(12)
tree.insert(node9)
node10=node(1)
tree.insert(node10)
tree.BFS()
