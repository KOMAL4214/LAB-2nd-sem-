class bankmanagement:
    def __init__(self,name,acctype,accbalance):
        self.accbalance=accbalance
        self.name=name
        self.acctype=acctype
    def withdraw(self):          
        g=int(input("enter the money to draw :"))
        if(g>self.accbalance):
            print("your account does not cantain this much money")
        else:
            print("you withdrawn :",g)
            print("after withdraw your balance is :",self.accbalance-g)
            self.accbalance=self.accbalance-g
    def deposit(self):
        g=int(input("enter the money to deposit :"))
        print("after deposit your account balance is :",self.accbalance+g)
        self.accbalance=self.accbalance+g
    def accountbalance(self):
        print("your account has balance of :",self.accbalance)
print("enter details to create account")
name=input("enter your name :")
acctype=input("enter account type :")
accbalance=int(input("enter the balance :"))
p1=bankmanagement(name,acctype,accbalance)   
print("choose:1->withdraw")
print("choose:2->deposit")
print("choose:3->check balance")
des=1
while(des):
    k=int(input("enter your choice :"))
    if(k==1):
        p1.withdraw()
    elif(k==2):
        p1.deposit()
    elif(k==3):
        p1.accountbalance()
    des=int(input("if want to continue type(1) else type(0)"))