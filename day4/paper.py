#!/usr/bin/env python3

import sys

def check_rolls(line_list: list[list]) -> int:
    '''
    Takes in matrix with 3 rows and checks the middle row for 
      eligible rows.
    '''
    eligible_rolls = 0

    row_len = len(line_list[1])
    for column_i in range(row_len):
        surround_list = list()
        if line_list[1][column_i] == '@':
            if column_i == 0:
                # populate list clockwise 0-6 o'clock only
                for row in range(3):
                    for column in [column_i, column_i+1]:
                        surround_list.append(line_list[row][column])
                rolls_around = surround_list.count('@') - 1

            elif column_i == row_len-1:
                # populate list clockwise 6-0 o'clock only
                for row in range(3):
                    for column in [column_i-1, column_i]:
                        surround_list.append(line_list[row][column])
                rolls_around = surround_list.count('@') - 1

            else:
                for row in range(3):
                    for column in [column_i-1, column_i, column_i+1]:
                        surround_list.append(line_list[row][column])
                rolls_around = surround_list.count('@') - 1
            
            if rolls_around < 4:
                eligible_rolls += 1

    return eligible_rolls

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
        print(*line_list,' ',sep="\n")
        answer += check_rolls(line_list)
        line_list = line_list[1:]
        line_list.append(line)
        line = list((input.readline()).strip())

    
    print(*line_list,' ',sep="\n")
    line_list = line_list[1:]
    line_list.append(buffer)
    print(*line_list,' ',sep="\n")
    answer += check_rolls(line_list)

print(f"{answer=}")
