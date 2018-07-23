#Importing nessasary modules
import random

#Initialising parameters
chances=10
points_computer=0
points_player=0
i=int(10)

while i>0:
    computer =['Rock','Paper', 'Scissors']
    b = random.choice(computer) # The computer chosses a random option
    print(b)
    a = input("enter Rock,Paper,Scissors ") # The users imput is given here

    if  a!=b:
        # The conditions wher the player wins
        if a=="Rock" and b=="Scissors":
            points_player+=1
            print(i-1, " chances left")

        elif a=="Scissors" and b=="Paper":
            points_player+=1

        elif a=="Paper" and b=="Rock":
            points_player+=1

        # The conditions wher the computer wins
        elif b=="Rock" and a=="Scissors":
            points_computer+=1

        elif b=="Scissors" and a=="Paper":
            points_computer += 1

        elif b=="Paper" and a=="Rock":
            points_computer += 1

    # when the user and the computer inputs the same option
    else:
        print("!!!....DRAW....!!!")


    #Printing the chances left , and the poits of the computer and player
        print(i - 1, " chances left")
    print("points_computer :  ",points_computer)
    print("points_player :  " , points_player)

    i-=1