import random


while True:
 choice=input("wanna role the dice ?(yes or no):").lower()
 if (choice=="yes"):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"({die1},{die2})")
 elif (choice=="no"):
    print("thank you for playing")
    break
 else:
    print("invalid input")





