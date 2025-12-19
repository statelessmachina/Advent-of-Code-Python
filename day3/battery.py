#!/usr/bin/env python3
import sys

answer = 0

with open(sys.argv[1], 'r') as file:
    line = file.readline()
    while line:
        numbers = [int(i) for i in list(line.strip())]
        max_num = max(numbers)
        max_idx = numbers.index(max_num)
        current_batt = 0
        if max_idx == len(numbers)-1:
            current_batt = ((max(numbers[:max_idx])*10) + max_num)

        else:
            current_batt = ((max_num * 10) + max(numbers[max_idx+1:]))
            
        answer += current_batt
        print(f'{numbers}')
        print(f'{current_batt=} :: {answer=}')
        line = file.readline()

    print(f'{answer=}')

