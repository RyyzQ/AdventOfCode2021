with open("day02/input.txt") as input:
    input_list = input.readlines()

def part1():
    pos = [0,0]
    for command in input_list:
        curr_command = command.split()
        if curr_command[0] == "forward":
            pos[0] = pos[0] + int(curr_command[1])
        elif curr_command[0] == "down":
            pos[1] = pos[1] + int(curr_command[1])
        elif curr_command[0] == "up":
            pos[1] = pos[1] - int(curr_command[1])
    
    print(f"Position at the end of part1: {pos}")
    print(f"Multiplied (X*Y): {pos[0] * pos[1]}")

def part2():
    pos = [0,0,0] # X, Y, Aim - horizontal pos, depth, aim
    for command in input_list:
        curr_command = command.split()
        if curr_command[0] == "forward":
            pos[0] = pos[0] + int(curr_command[1])
            pos[1] = pos[1] + (pos[2] * int(curr_command[1]))
        elif curr_command[0] == "down":
            pos[2] = pos[2] + int(curr_command[1])
        elif curr_command[0] == "up":
            pos[2] = pos[2] - int(curr_command[1])
    
    print(f"Position at the end of part2: {pos}")
    print(f"Multiplied (X*Y): {pos[0] * pos[1]}")

part1()
part2()