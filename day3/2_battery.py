#!/usr/bin/env python3

answer = 0

with open('input', 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        numbers = [int(i) for i in list(line)]
        max_num = max(numbers[:-12])
        max_idx = numbers.index(max_num)
        current_batt = 0

        if max_idx == 88:
            current_batt = int(line[88:])

        else:
            current_batt = numbers[max_idx:]
            min_num = 0
            while len(current_batt) > 12:
                min_num = min(current_batt)
                current_batt.remove(min_num)
            
            temp_ans = ''
            for i in current_batt:
                temp_ans += str(i)

            current_batt = int(temp_ans)

        answer += current_batt
        print(f'{numbers}')
        print(f'{current_batt=} :: {answer=}')
        line = file.readline()

    print(f'{answer=}')

