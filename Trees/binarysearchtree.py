class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class Btree:
    def __init__(self):
        self.root=None
        self.deleted=False
    def insert(self,newnode):
        if self.root is None:
            self.root=newnode
            print('inserted')
        else:
            temp=self.root
            while True:
                if newnode.data>=temp.data:
                    if temp.right is None:
                        break
                    temp=temp.right
                else:
                    if temp.left is None:
                        break
                    temp=temp.left
            if newnode.data>=temp.data:
                temp.right=newnode
            else:
                temp.left=newnode
            print('inserted')
    def search(self,key):
        temp=self.root
        while temp != None:
            if key == temp.data:
                print('found')
                break
            elif key > temp.data:
                temp=temp.right
            else:
                temp=temp.left
        else:
            print('not found')
    def delete(self,key):
        temp=self.root
        while temp != None:
            if key == temp.data:
                if temp.left==None and temp.right == None:# case(i) : i.e if the node is a leaf-node
                    x=temp
                    temp=self.root
                    while temp.left!=x and temp.right!=x:
                        if key<temp.data:
                            temp=temp.left
                        else:
                            temp=temp.right
                    if temp.left ==x:
                        temp.left=None
                    else:
                        temp.right=None
                    self.deleted=True
                    break
                elif temp.left ==None or temp.right==None:#case(ii): if the node has ONE child
                    if temp.left==None:
                        temp.data=temp.right.data
                        temp.right=None
                    else:
                        temp.data=temp.left.data
                        temp.left=None
                    self.deleted=True
                    break
                else:#case (iii): when the node has two children
                    x=temp
                    temp=temp.right
                    while temp.left!=None:
                        if temp.left.left is None:
                            y=temp
                        temp=temp.left
                    x.data=temp.data#replacing with succesor node's value
                    if y.left.right is None:
                        y.left=None
                    else:
                        y.left=y.left.right
                    self.deleted=True
                    break
            elif key > temp.data:
                temp=temp.right
            else:
                temp=temp.left
        if self.deleted==True:
            print('deleted')
        else:
            print('element not found')
    def display(self,rootnode):
        if rootnode is None:
            return
        self.display(rootnode.left)
        print(rootnode.data)
        self.display(rootnode.right)
    def bruh(self):
        temp = self.root
        def valid(temp,l,u):
            if not temp:
                return []
            if l<temp.data<u:
                return [temp] + valid(temp.left,l,temp.data) + valid(temp.right,temp.data,u)
        x = valid(temp,float('-inf'),float('inf'))
tree=Btree()
node1=node(9)
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
tree.bruh()
