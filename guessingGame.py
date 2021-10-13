import random
number = random.randint(1, 9)
chances = 5
guess = input("Guess a number between 1 and 9: ")
if(guess<number):
    chances = chances - 1
    print("Your guess is too low")
elif(guess>number):
    chances = chances - 1
    print("Your guess is too high")

if(guess == number):
    print("Congratulations!! You Won!!")

if(chances == 0):
    print("You Lose!! " + "The correct number is: " + number)
