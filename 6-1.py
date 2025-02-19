class Password_Manager:
    global oldpasswords
    oldpasswords=[]
    def getpassword():
        print(oldpasswords[len(oldpasswords)-1])
    def setpassword(k):
        if(len(oldpasswords)==0):
            oldpasswords.append(k)
        else:
            if(k in oldpasswords):
                    print("password already present")
                    p1.setpassword(input("enter the password :"))
            else:
                oldpasswords.append(k)
    def isright(k):
        if(k==oldpasswords[len(oldpasswords)-1]):
            print("true")
        else:
            print("false")
p1=Password_Manager
print("1->getpassword")
print("2->setpassword")
print("3->isright")
print("0->end process")
ch=int(input("enter your choice :"))
while(ch):
    match ch:
        case 1:p1.getpassword()
        case 2:p1.setpassword(input("enter the password :"))
        case 3:p1.isright(input("enter the password :"))
    ch=int(input("enter your choice :"))



