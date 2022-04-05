#Creating a tree first using my code and then traversing it in a DFS fashion
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
    def DFS(self):
        #iterative(PREORDER)
        """
        if not self.root:
            return []
        stack = [self.root]
        result = []
        while len(stack) != 0:
            x = stack.pop()
            result.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        for i in result:
            print(i)
        #recursive(preorder)
        if not root:
            return []
        return [root.val]+func_name(root.left)+func_name(root.right)
        """
        #iterative(POSTORDER)
        """
        # Note that this iterative code cannot handle duplicates !!!!!!!!!
        stack = [self.root]
        visited=[]
        while len(stack) != 0:
            x = stack[-1]
            if x.left and x.left.val not in visited:
                stack.append(x.left)
            elif x.right and x.right.val not in visited:
                stack.append(x.right)
            elif not x.left and not x.right:
                y=stack.pop()
                visited.append(y.val)
            else:
                y=stack.pop()
                visited.append(y.val)
        for i in visited:
            print(i)
        #recursive(POSTORDER)
        if not root:
            return []
        return func_name(root.left)+func_name(root.right)+[root.val]
        """
        #iterative(INORDER)
        if not root:
            return []
        stack = []
        result = []
        while root or len(stack) != 0:
            while root!=None:
                stack.append(root)
                root = root.left
            x = stack.pop()
            result.append(x.val)
            root = x.right
        return result
        #recursive(INORDER)
        if not root:
            return []
        return func_name(root.left)+[root.val]+func_name(root.right)
tree = Tree()
node1 = node(10)
tree.insert(node1)
node2=node(15)
tree.insert(node2)
node3=node(14)
tree.insert(node3)

tree.DFS()
