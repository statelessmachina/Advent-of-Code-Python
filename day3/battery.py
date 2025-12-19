#!/usr/bin/env python3
import sys

answer = 0

if len(sys.argv) > 2:
    battery_len = int(sys.argv[2])
else:
    battery_len = 2

with open(sys.argv[1], 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()                             # strips '\n'
        numbers = [int(i) for i in list(line)]          # Turns input str of digits into int 
        max_num = max(numbers[:-battery_len])           # finds max digit in subset of num list, 
                                                        # from beginning to end minus battery_len from the end
        max_idx = numbers.index(max_num)
        current_batt = 0

    # This if/else checks index of the max_number in the list
        last_digit_check = len(line)-battery_len        # Biggest index the max could be to return 
                                                        #  the target battery length.
        if max_idx == last_digit_check:                 # If the index is located less than target battery length
            current_batt = int(line[last_digit_check:]) #  from the end, it just prints the last "battery_len" digits.

        else:                               
            current_batt = numbers[max_idx:]            # Grabs subset of numbers starting at first max found
            min_num = 0                                 #  then starts looking for the min digit and removes 
            while len(current_batt) > battery_len:      #  until the len(current_batt) is equal to the target length
                min_num = min(current_batt)
                current_batt.remove(min_num)

            temp_ans=''                                 # Concatenates each number together as a str then casts to int
            for i in current_batt:
                temp_ans += str(i)

            current_batt = int(temp_ans)
            
        answer += current_batt                          # Adds final battery to answer 
        line = file.readline()                          #  and reads next line
        #print(f'{numbers}')                            # Debug statements
        #print(f'{current_batt=} :: {answer=}')

    print(f'{answer=}')

