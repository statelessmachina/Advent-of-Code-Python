#!/usr/bin/env python3

with open("input","r") as file:
	lines = file.readlines()

answer=0
for line in lines:
	line = [i.strip('\n') for i in line.split("-")]
	start = line[0]
	end = line[1]

	if not len(start)%2 or not len(end)%2:
		for num in range(int(start),int(end)):
			num = str(num)
			if not len(num)%2 and num[:len(num)//2] == num[len(num)//2:]:
				answer += int(num)
				

print(f'{answer=}')
