from random import *
from copy import *


def score_cal(n1,n2,n3,n4,n5):
    if n3 == n1:
        print("You have guessed the number correctly. You won the game.")
        return 1
    else:
        for i in range(0, 4):
            if n3[i] in n2:
                if n3[i] == n1[i]:
                    n4.append(n3[i])
                else:
                    n5.append(n3[i])
                n2[n2.index(n3[i])] = -35487
        print(len(n4), " correct digits at correct position: ", n4)
        print(len(n5), " correct digits at wrong position ", n5)
        return 0


def result(ch):
    while ch == 1:
        ran, score = randint(1000, 9999), 20
        n1, no_of_guesses = [int(i) for i in str(ran)], 10
        while no_of_guesses > 0:
            n2, n4, n5 = deepcopy(n1), [], []
            guess = int(input("Guess the 4 digit number : "))
            n3 = [int(i) for i in str(guess)]

            rtd=score_cal(n1, n2, n3, n4, n5)

            if(rtd==1):
                score+=5
                break
            else:
                score-=2
            no_of_guesses -= 1
            print("Sorry wrong number. Guess again.\nGuesses left : ",no_of_guesses )

        print("Your score is : ", score)
        ch = int(input("You have finished the game. Do you want to play again?\n1 - Yes\n0 - No\n"))


result(ch = int(input("Do you want to play the MASTERMIND GAME?\n1 - Yes\n0 - No\n")))
