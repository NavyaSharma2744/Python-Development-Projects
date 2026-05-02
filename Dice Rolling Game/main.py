import random

string = input("Roll the dice(y/n)?")


Dice = [1,2,3,4,5,6]

if string == 'y' :
    print(random.sample(Dice, 2))
elif string == 'n' :
    print("Thanks for playing.")
else:
    print("Invalid input!")     

