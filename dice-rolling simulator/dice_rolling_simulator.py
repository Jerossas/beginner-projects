import random

def roll_dice():
    dice_number = random.randint(1, 6)
    print(f"Gotten number > {dice_number}")


while True:
    print("\t1. roll\n\t2. exit")
    user_input = input("select an option(1|2) >>> ")

    if user_input == "1":
        roll_dice()
    elif user_input == "2":
        break