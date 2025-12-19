#!/usr/bin/env python3

state = 50
answer = 0
prev_state = 0

with open("input", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    prev_state = state
    direction = line[0]
    
    if direction == "R":
        state += int(line[1:])

    elif direction == "L":
        state -= int(line[1:])

    if state < 1 or state > 99:
        answer += abs(state//100)
        if prev_state == 0:
            answer -= 1
    
    state = state%100

    print(f'{prev_state} {direction} {line[1:]} :: {state} :: {answer=}')
print(f'{answer=}')
