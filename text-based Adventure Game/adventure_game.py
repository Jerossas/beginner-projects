
instructions = """\
\n
How to play?

    There's gonna be a displayed map on your screen, and the goal is to get to a position on the matrix where the value of that position is 2. Yoou are the '3' on the matrix

commands 

    -mr num
        mr stands for move right and num is number of steps you wanna take.

    -ml num
        The same shit as before but left

    -md num
        the same shit as before but down

    -mu num
        the same shit as before but up

That's all!! Lets get started!
"""

map = [
    [1,1,1,1,1,1,1,1],
    [1,3,1,1,2,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]

character_position = [1, 1]
final_position = [4, 1]

def print_map():
    print("[MAP]")
    for row in map:
        print(*row)
    
def play():
    print_map()
    while character_position != final_position :
        print("----------------------------------------------------------")
        player_input = input("Enter a command >>> ").split()
        c = player_input[0]

        if c == "-md":
            dy = character_position[1]+int(player_input[1])
            if dy < len(map):
                map[character_position[1]][character_position[0]] = 0
                character_position[1] = dy
                map[character_position[1]][character_position[0]] = 3
            elif dy >= len(map)-1:
                print("** Character out of bounds! **")
                print("** the command hasn't been executed. You are at the same position as before **")
        elif c == "-mr":
            dx = character_position[0]+int(player_input[1])
            if dx < len(map[0])-1:
                map[character_position[1]][character_position[0]] = 0
                character_position[0] = dx
                map[character_position[1]][character_position[0]] = 3
            elif dx >= len(map[0])-1:
                print("** Character out of bounds! **")
                print("** the command hasn't been executed. You are at the same position as before **")
        elif c == "-mu":
            dy = character_position[1]-int(player_input[1])
            if dy > 0:
                map[character_position[1]][character_position[0]] = 0
                character_position[1] = dy
                map[character_position[1]][character_position[0]] = 3
            elif dy <= 0:
                print("** Character out of bounds! **")
                print("** the command hasn't been executed. You are at the same position as before **")
        elif c == "-ml":
            dx = character_position[0]-int(player_input[1])
            if dx > 0:
                map[character_position[1]][character_position[0]] = 0
                character_position[0] = dx
                map[character_position[1]][character_position[0]] = 3
            elif dx <= 0:
                print("** Character out of bounds! **")
                print("** the command hasn't been executed. You are at the same position as before **")

        print(f"Current position {character_position}")
        print_map()
    print("** !!YOU HAVE WON THE GAME MOTHERFUCKER!! **")

while True:

    options = ("""\n\n\n\
    1. Play
    2. look instructions
    3. Exit
    """)
    print(options)

    user_input = input("Select an option (1|2|3): ")

    if user_input == "1":
        play()
    elif user_input == "2":
        print(instructions)
    elif user_input == "3":
        break
    else:
        print("You've selected an invalided option")

