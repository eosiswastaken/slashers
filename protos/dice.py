import random

def simple_dice():
    return ("[ " + str(random.randint(1,6)) + " ]")

def simple_coin(head,tails):
    return ("[ " + (("Heads " + str(head)) if random.randint(1,2) == 2 else ("Tails " + str(tails))) + " ]")



def coin(head,tails):
    if random.randint(1,2) == 1:
        return("Tails",tails)
    else:
        return("Head",head)

def dice(sides,mana):
    roll = random.randint(1,6)
    return(sides[roll-1],mana[roll-1])


def shop():
    print(" - What action do you want to do ? (" + str(total) + " mana left)")
    bought = False
    while not bought:
        pass
#for i in range(10):
#    print(dice())
total = 0
for i in range(3):
    roll = dice([1,2,3,4,5,6],[1,2,3,4,5,6])
    print("You rolled a [ " + str(roll[0]) + " ] , and gained " + str(roll[1]) + " mana !")
    total += roll [1]
print("Total mana :" + str(total))
shop()

