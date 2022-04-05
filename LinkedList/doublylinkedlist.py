class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertEnd(self,newnode):
        if self.head is None:
            self.head=newnode
            print('element inserted')
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
            self.tail=newnode
            self.tail.prev=temp
            print('element inserted')
    def insertBeg(self,newnode):
        if self.head is None:
            self.head=newnode
            print('element inserted')
        else:
            newnode.next=self.head
            self.head=newnode
            print('element inserted')
    def deleteEnd(self):
        if self.head is None:
            print('list is empty')
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            print('element deleted')
    def deleteBeg(self):
        if self.head is None:
            print('list is empty')
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            print('element deleted')
    def insertpos(self,newnode,pos):
        if pos == 1:
            insertBeg(self,newnode)
        else:
            curr=self.head
            for i in range(pos-2):
                curr=curr.next
            newnode.prev=curr
            newnode.next=curr.next
            curr.next=newnode
            print('element inserted')
    def deletepos(self,pos):
        if pos==1:
            deleteBeg(self)
        else:
            curr=self.head
            for i in range(pos-2):
                curr=curr.next
            curr.next=curr.next.next
            curr.next.next.prev=curr
            curr.next.next=None
            curr.next.prev=None
            print('element deleted')
    def printlist(self):
        if self.head is None:
            print('list is empty')
        else:
            temp=self.head
            while temp.next != None:
                print(f'{temp.data}--->',end='')
                temp=temp.next
            print(f'{self.tail.data}')
    def xyz(self):
        print(f'last element is {self.tail.data} and prev element is {self.tail.prev.data}')
list=Linkedlist()
"""end insertion"""
newNode1=Node(1)
list.insertEnd(newNode1)
newNode2=Node(2)
list.insertEnd(newNode2)
newNode3=Node(3)
list.insertEnd(newNode3)
list.printlist()
list.xyz()

"""insertion at beginning"""
newnode4=Node(4)
list.insertBeg(newnode4)
newnode5=Node(5)
list.insertBeg(newnode5)
list.printlist()
list.xyz()

"""delete at end"""
list.deleteEnd()
list.printlist()
list.xyz()

"""delete at beginning"""
list.deleteBeg()
list.printlist()
list.xyz()

"""insert at position"""
newnode6=Node(6)
list.insertpos(newnode6,2)
list.printlist()
list.xyz()

"""delete at pos"""
list.deletepos(3)
list.printlist()
list.xyz()
