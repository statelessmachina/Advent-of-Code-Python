#!/usr/bin/env python3

import sys

def can_get_roll(line_list: list[list], roll_i: int) -> bool:
    surround_list = list()
    row_len = len(line_list[1])
    if roll_i == 0:
        # populate list clockwise 0-6 o'clock only
        for row in range(3):
            for column in [roll_i, roll_i+1]:
                surround_list.append(line_list[row][column])
        rolls_around = surround_list.count('@') - 1
        rolls_around += surround_list.count('X')

    elif roll_i == row_len-1:
        # populate list clockwise 6-0 o'clock only
        for row in range(3):
            for column in [roll_i-1, roll_i]:
                surround_list.append(line_list[row][column])
        rolls_around = surround_list.count('@') - 1
        rolls_around += surround_list.count('X')

    else:
        for row in range(3):
            for column in [roll_i-1, roll_i, roll_i+1]:
                surround_list.append(line_list[row][column])
        rolls_around = surround_list.count('@') - 1
        rolls_around += surround_list.count('X')

    if rolls_around < 4:
        return True
    else: 
        return False


answer = 0 
with open(sys.argv[1], 'r') as input:
    # Grabs first 2 line_list to start checking rolls
    # Initializes with one empty row to check top row
    line = list((input.readline()).strip())
    buffer = list('.' * len(line))
    line_list = [buffer]
    for i in range(2):
        line_list.append(line)
        line = list((input.readline()).strip())

    while line:
        num_columns = len(line_list[1])
        for i in range(num_columns):
            if line_list[1][i] == '@' and can_get_roll(line_list, i):
                answer += 1
                line_list[1][i] = 'X'
                
        print(''.join(line_list[1]),sep="\n")
        line_list = line_list[1:]
        line_list.append(line)
        line = list((input.readline()).strip())

    
    print(''.join(line_list[1]),sep="\n")
    line_list = line_list[1:]
    line_list.append(buffer)
    #print(*line_list,' ',sep="\n")

    num_columns = len(line_list[1])
    for i in range(num_columns):
        if line_list[1][i] == '@' and can_get_roll(line_list, i):
            answer += 1
            line_list[1][i] = 'X'
    print(''.join(line_list[1]),sep="\n")

print(f"{answer=}")
