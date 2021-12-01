with open("day01/input1.txt") as input:
    input_list = input.readlines()

input_list = [int(item) for item in input_list]

def part1():
    increase_amount = 0
    prev_num = None

    for item in input_list:
        if prev_num is not None:
            increase_amount = increase_amount+1 if item > prev_num else increase_amount

        prev_num = item

    print(f"part 1: {increase_amount}")

def part2():
    increase_amount = 0
    prev_num = None

    for i in range(0, len(input_list)):
        if i+2 >= len(input_list):
            continue
        else:
            sum_value = input_list[i] + input_list[i+1] + input_list[i+2]
        if prev_num is not None:
            increase_amount = increase_amount+1 if sum_value > prev_num else increase_amount

        prev_num = sum_value

    print(f"part 2: {increase_amount}")

part1()
part2()