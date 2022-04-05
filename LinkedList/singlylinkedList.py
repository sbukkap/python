class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertEnd(self,newnode):
        if self.head is None: #if list is empty
            self.head=newnode
            print('element inserted')
        else:                 #has atleast one element
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=newnode
            print('element inserted')
            self.tail=temp.next
    def insertBeg(self,newnode):
        if self.head == None: #if list is empty
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def deleteEnd(self):
        if self.head == None:
            print('list empty')
        else:
            temp=self.head
            while temp.next != self.tail:
                temp=temp.next
            temp.next=None
            self.tail=temp
            print('element deleted')
    def deleteBeg(self):
        if self.head == None:
            print('list empty')
        else:
            self.head=self.head.next
            print('element deleted')
    def insertpos(self,newnode,pos):
        if pos==1:
            insertBeg(self,newnode)
        else:
            temp=newnode
            curr=self.head
            for i in range(pos-2): #arriving at prev. position for given pos
                curr=curr.next
            temp.next=curr.next
            curr.next=temp
            print('element inserted')
    def deletepos(self,pos):
        if self.head == None:
            print('list empty')
        elif pos==1:
            deleteBeg(self)
        else:
            curr=self.head
            for i in range(pos-2):
                curr=curr.next
            curr.next=curr.next.next
            curr.next.next=None
            print('element deleted')
    def lastandfirst(self):
        print(f'the data at last node is {self.tail.data} and the data at first node is{self.head.data}')
    def printlist(self):
        if self.head == None:
            print('list empty')
        else:
            temp=self.head
            while temp.next != None:
                print(f'{temp.data}-->',end=' ')
                temp=temp.next
            print(self.tail.data)
list=Linkedlist()
"""end insertion"""
newNode1=Node(1)
list.insertEnd(newNode1)
newNode2=Node(2)
list.insertEnd(newNode2)
newNode3=Node(3)
list.insertEnd(newNode3)
list.printlist()

"""insertion at beginning"""
newnode4=Node(4)
list.insertBeg(newnode4)
newnode5=Node(5)
list.insertBeg(newnode5)
list.printlist()

"""delete at end"""
list.deleteEnd()
list.printlist()

"""delete at beginning"""
list.deleteBeg()
list.printlist()

"""insert at position"""
newnode6=Node(6)
list.insertpos(newnode6,2)
list.printlist()

"""delete at pos"""
list.deletepos(3)
list.printlist()
