#!/usr/bin/env python3

with open("input","r") as file:
    lines = file.readlines()

answer=0
for line in lines:
    line = [i.strip('\n') for i in line.split("-")]
    start = line[0]
    end = line[1]

    group_len=0

    for num in range(int(start),int(end)):
        num = str(num)
        if len(num)>1:
            for group_len in range(1,len(num)):
                num_set=set([num[i:i+group_len] for i in range(0,len(num),group_len)])
                if len(num_set) == 1:
                    #print(f'{num}')
                    answer += int(num)
                    break
            

print(f'{answer=}')
