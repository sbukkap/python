class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,newnode):
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            print(f'{self.head.data} has been pushed')
        else:
            newnode.next=self.head
            self.head=newnode
            print(f'{self.head.data} has been pushed')
    def pop(self):
        if self.head is None:
            print('stack is empty')
        else:
            temp=self.head
            self.head=self.head.next
            print(f'{temp.data} is popped')
            temp.next=None
    def display(self):
        if self.head is None:
            print('stack is empty')
        else:
            temp=self.head
            while temp.next!= None:
                print(f'{temp.data}-->',end='')
                temp=temp.next
            print(self.tail.data)
s=Stack()
node1=Node(1)
s.push(node1)
node2=Node(2)
s.push(node2)
node3=Node(3)
s.push(node3)
node4=Node(4)
s.push(node4)
s.display()

s.pop()
s.pop()
s.display()
s.pop()
s.pop()
s.pop()
s.display()
