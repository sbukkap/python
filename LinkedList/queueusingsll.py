class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def isEmpty(self):
        return self.head == None
    def enqueue(self,newnode):
        if self.isEmpty():
            self.head=newnode
            self.tail=newnode
            print('done')
        else:
            self.tail.next=newnode
            self.tail=newnode
            print('done')
    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
        else:
            self.head=self.head.next
            print('doen')
    def fandl(self):
        print(f'first node is {self.head.data} and last node is{self.tail.data}')
queue=Queue()
node1=Node(1)
queue.enqueue(node1)
node2=Node(2)
queue.enqueue(node2)
node3=Node(3)
queue.enqueue(node3)
node4=Node(4)
queue.enqueue(node4)
queue.dequeue()
queue.dequeue()
queue.fandl()
