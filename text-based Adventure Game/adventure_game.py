

presentation = """\
\n  
WELCOME TO SURVIVE TO THE MATRIX XD

How to play?

    There's gonna be a displayed map on your screen, and the goal is to get to a position on the matrix where the value of that position is 2. Yoou are the '3' on the matrix

commands 

    -mr num
        mr stands for move right and num is number of steps you wanna take.

    -ml num
        The same shit as before but left

    -md 
        the same shit as before but down

    -mu 
        the same shit as before but up

That's all!! Lets get started!
"""

print(presentation + "\n")
initial_position = (1, 1)
setting = [
    [1,1,1,1,1,1,1,1],
    [1,3,1,1,2,0,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]

def print_map():
    for row in setting:
        print(*row)

def move():
    user_input = input("Enter a command >> ").split()

    if user_input[0] == "-mr":
        new_position = (initial_position[0]+int(user_input[1]), initial_position[1])
        print(new_position)

        setting[initial_position[1]][initial_position[0]] = 0
        setting[new_position[1]][new_position[0]] = 3

print_map()
move()
print_map()