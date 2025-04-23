import random

n= random.randint(1,100)

a=-1

guess=0

while(a!=n):
    guess= guess + 1
    a=int(input("guess a number from 1 to 100  "))
    
    if(a<n):
        print("please select a higher number")
        
    else:
        print("please select a lower number")
    
print("you have guessed the correct number in ", guess, "attempts")