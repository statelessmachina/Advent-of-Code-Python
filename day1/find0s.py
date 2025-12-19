#!/usr/bin/env python3

state = 50
answer = 0

with open("input", "r") as file:
	lines = file.readlines()

for line in lines:
	#print(line)
	if line[0] == "R":
		state += int(line[1:].strip('\n'))

	elif line[0] == "L":
		state -= int(line[1:].strip('\n'))
	
	if state%100 == 0:
		answer += 1

#	print(f'{line=} :: {state=} :: {answer=}')
print(f'{answer=}')
