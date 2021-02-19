import random

def main():
    
    dice_roll = 2
    dice_sum = 0
    for i in range(0,dice_roll):
        roll = random.randint(1,6)
        dice_sum += roll
        print("You rolled a {}".format(roll))
    print("You have rolled a total of {}".format(dice_sum))

if __name__== "__main__":
  main()
