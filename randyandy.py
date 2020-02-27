import random

def inpy(prompy):
    try:
        return int(input(prompy))
    except:
        print("please enter a number")
        return inpy(prompy)
    
randy=random.randint(0,100)
andy=inpy("what number am I thinking of?")
numby=0

while True:
    numby+=1
    if andy==randy:
        print("well done!")
        print("number of attempts:",numby)
        break
    elif andy>randy:
        print("too high!")
    else:  
        print("too low!")
    andy=inpy("")

filly=open("output.txt", "w")
filly.write("it took " + str(numby) + " tries")
filly.close()
