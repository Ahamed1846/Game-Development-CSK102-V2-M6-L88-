from random import randint
comp = ["rock", "paper", "scissors"]
compInp=0
playerScore=0
compScore=0
player = True

print('\nScore 5 points to win\n')

while player == True:
    playerInp = input("\nEnter your choice (rock, paper, scissors)=")
    compInp = comp[randint(0,2)]
    if playerInp == compInp:
        print('\nYour input:',playerInp,'\n\nComputer:',compInp,"\n\nTie!")
    elif playerInp == "rock":
        if compInp == "paper":
            compScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the computer\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
        else:
            playerScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the player\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
    elif playerInp == "paper":
        if compInp == "scissors":
            compScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the computer\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
        else:
            playerScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the player\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
    elif playerInp == "scissors":
        if compInp == "rock":
            compScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the computer\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
        else:
            playerScore+=1
            print('\nYour input:',playerInp,'\n\nComputer:',compInp,'\n\nThe point goes to the player\n','\nPlayer score=',playerScore,'\n\nComputer score=',compScore)
    else:
        print("That's not a valid play. Check your spelling!")
    if playerScore==5 or compScore==5:
        player = False
if playerScore==5:
    print('\nYou won!')
else:
    print('\nYou lose!')