import random

print("Welcome Rock Paper Scissors!")
print("!---------------!")
compscore=0
playerscore=0
tiescore=0
possibleHands=["Rock","paper","Scissor"]
def check_winner(user_hand,comp_hand):
    if(user_hand=="Rock" and comp_hand=="paper"):
        print("sorry you lost and computer won the game")
        return "computer"
    elif(user_hand=="Rock"and comp_hand=="Scissor"):
        print("!...Congratulation you won the game...!")
        return "player"
    elif(user_hand=="Scissor" and comp_hand=="Rock"):
        print("sorry you lost and computer won the game")
        return "computer"
    elif(user_hand=="Scissor"and comp_hand=="paper"):
        print("!...Congratulation you won the game...!")
        return "player"
    elif(user_hand=="paper"and comp_hand=="Rock"):
        print("!...Congratulation you won the game...!")
        return "player"
    elif(user_hand=="paper" and comp_hand=="Scissor"):
        print("sorry you lost and computer won the game") 
        return "computer"
    else:
        print("It is a tie,play again...")
while(playerscore!=5 and compscore!=5):
    while True:
            user_hand = input("pick a hand: rock ,scissor or paper")
            if(user_hand == "Rock" or user_hand == "Scissor" or user_hand == "paper" ):
                break
            else:
                print("Invalid input. Try again.")
    comp_hand=random.choice(possibleHands)
    print("User hand:",user_hand)        
    print("Computer hand",comp_hand)
    result=check_winner(user_hand,comp_hand)
    if(result=="player"):
      playerscore +=1
    elif(result=="computer"):
       compscore +=1
    else:
       tiescore +=1
    print("userscore:",playerscore, "computerscore:",compscore, "tiescore:",tiescore )
print("!...Game is over...!")
print("Thank You for playing game")