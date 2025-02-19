import random
class rockpaperscissors:
    global rounds
    rounds=int(input("enter the number of rounds :"))
    currrentround=0
    global cwins
    cwins=0
    global uwins
    uwins=0
    def computerchoice():
        def winnerofround(rounds,uwins,cwins):
            while(rounds>0):
                j=int(input("enter the choice of user :"))
                k=random.choice([1,2,3])
                if(k==1):
                    print("the computer choose rock")
                elif(k==2):
                    print("the computer choose paper")
                else:
                    print("the computer choose scissors")
                if(j==1):
                    if(k==3):
                        print("user won the round")
                        uwins+=1
                    elif(k==2):
                        print("computer won the round")
                        cwins+=1
                    else:
                        print("both choose same choice")
                elif(j==3):
                    if(k==1):
                        print("computer won the round")
                        cwins+=1
                    elif(k==2):
                        print("user won the round")
                        uwins+=1
                    else:
                        print("both choose same option")
                elif(j==2):
                    if(k==3):
                        print("computer won the round")
                        cwins+=1
                    elif(k==1):
                        print("user won the round")
                        uwins+=1
                    else:
                        print("both choose same option")
                else:
                    print("user choose wrong choice")
                    print("the game is terminated!!!!!!!!!!!!!!!!!")
                    exit(0)
                rounds-=1
            def winnerofgame(cwins,uwins):
                if(uwins==cwins):
                    print("the game is a draw")
                elif(uwins>cwins):
                    print("user won the game")
                else:
                    print("computer won the game")
            print(uwins,cwins)
            winnerofgame(cwins,uwins)
        winnerofround(rounds,uwins,cwins)
rps=rockpaperscissors
print("choose 1->rock")
print("choose 2->paper")
print("choose 3->scissors")
rps.computerchoice()    


