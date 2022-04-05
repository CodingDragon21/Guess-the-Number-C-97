from random import randint


randomNumber = randint(1,20)
chances = 5

print("I have a number in my head that is between 1 and 20. Try To Guess it!!!")
while chances > 0:
    guess = float(input("My guess is: "))
    if guess > randomNumber:
        print( guess, "is too high, try a lower number")
        chances = chances - 1
    elif guess < randomNumber:
        print(guess, "is too low, try a higher number")
        chances = chances - 1
    
    else:
        print("Congratualations!!! You found the secret number")
        print("You took", chances ,"tries")

        break
    

if chances == 0:
    ("You Loose! The number was", randomNumber)
