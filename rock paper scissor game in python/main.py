import  random

print("welcome to play rock, paper, sciscor")

computer = random.choice([1, 0, -1])

youstring = input("choose rock paper scissor \n")

dictionary = {"rock":1, "paper":0 ,"scissor":-1}

you = dictionary[youstring]

reversedictionary = {1:"rock", 0:"paper" ,-1:"scissor"}

print("you chose "+reversedictionary[you])

print("computer chose "+ reversedictionary[computer])

if(you==computer):
    print("its a draw")
else:
    if(you==1 and computer==0):
        print("computer wins")
    
    elif(you==0 and computer==1):
        print("you wins")
    
    elif(you==-1 and computer==1):
        print("computer wins")
    
    elif(you==1 and computer==-1):
        print("you wins")
    
    elif(you==0 and computer==-1):
        print("computer wins")
    
    elif(you==-1 and computer==0):
        print("you wins")
    
    else:
        print("invalid")
