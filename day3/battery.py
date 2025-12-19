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
        line = line.strip()
        numbers = [int(i) for i in list(line.strip())]
        max_num = max(numbers[:-battery_len])
        max_idx = numbers.index(max_num)
        current_batt = 0

        last_digit_check = len(line)-battery_len
        if max_idx == last_digit_check:
            #current_batt = ((max(numbers[:max_idx])*10) + max_num)
            current_batt = int(line[last_digit_check:])

        else:
            #current_batt = ((max_num * 10) + max(numbers[max_idx+1:]))
            current_batt = numbers[max_idx:]
            min_num = 0
            while len(current_batt) > battery_len:
                min_num = min(current_batt)
                current_batt.remove(min_num)

            temp_ans=''
            for i in current_batt:
                temp_ans += str(i)

            current_batt = int(temp_ans)
            
        answer += current_batt
        print(f'{numbers}')
        print(f'{current_batt=} :: {answer=}')
        line = file.readline()

    print(f'{answer=}')

