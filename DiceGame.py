import random
import random as rd

print('Rolling dice...')

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("Die 1: "+str(dice1))
print("Die 2: "+str(dice2))

total = dice1+dice2
print("Total value: "+str(total))

#Judgement
if total>=7:
    print("You won")
else:
    print("You lost")