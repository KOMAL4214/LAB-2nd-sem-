class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,x):
        newnode=node(x)
        if(self.rear == None):
            self.front=self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        temp=self.front
        del temp
        self.front=self.front.next
    def top(self):
        print(self.front.data)
    def display(self):
        while(self.front!=None):
            print(self.front.data)
            self.front=self.front.next
q=queue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.top()
q.display()