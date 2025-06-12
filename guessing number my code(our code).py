import random
answer=random.randint(1,100)
while True:
 guess=int(input("guess a number between 1-100:"))
 if guess>100 or guess<1:
    print("invalid number")
 elif guess > answer:
    print("too high!")
 elif guess < answer:
    print("too low")
 elif guess==answer:
    print ("congratulation brotha ")
    break



