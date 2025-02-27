class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def display(head):
        while(head != None):
            print(head.data)
            head=head.next
    def insertatfront(head):
        x=int(input("enter the data of the node :"))
        newnode=node(x)
        newnode.next=head
        return newnode
    def insertatend(head):
        while(head.next !=None):
            head=head.next
        x=int(input("enter the data of the node :"))
        newnode=node(x)
        head.next=newnode
    def deleteatend(head):
        while(head.next.next !=None):
            head=head.next
        head.next=None
    def deleteatfront(head):
        temp=head
        del temp
        return head.next
head=node(40)
head.next=node(10)
head.next.next=node(20)
head.next.next.next=node(30)
head.display()
print("\t")
head=head.insertatfront()
head.display()
head.insertatend()
print("\t")
head.display()
head.deleteatend()
print("\t")
head.display()
head=head.deleteatfront()
print("\t")
head.display()