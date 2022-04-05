class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Reverse:
    def __init__(self):
        self.head=None
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
    def reverse(self):
        temp=self.head
        prev=None
        curr=self.head
        self.tail=self.head
        while curr!=None:
            curr=curr.next
            temp.next=prev
            prev=temp
            temp=curr
        self.head=prev
    def printlist(self):
        if self.head == None:
            print('list empty')
        else:
            temp=self.head
            while temp.next != None:
                print(f'{temp.data}-->',end=' ')
                temp=temp.next
            print(self.tail.data)
list=Reverse()
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
list.reverse()
list.printlist()
