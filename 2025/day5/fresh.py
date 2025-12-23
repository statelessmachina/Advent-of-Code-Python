#!/usr/bin/env python3

import sys
from collections import deque

def is_overlapping(range1: range, range2: range) -> bool:
    '''
    Checks of 2 ranges overlap.
    '''
    if len(range1) == 0 or len(range2) == 0:
        return False
    start1, end1 = (min(range1), max(range1))
    start2, end2 = (min(range2), max(range2))
    return max(start1, start2) <= min(end1, end2)

def min_max(range1: range, range2: range) -> range:
    '''
    Returns range object starting at the min of 2 ranges
    and ending at the max of 2 ranges, inclusive (+1)
    '''
    start1, end1 = (min(range1), max(range1))
    start2, end2 = (min(range2), max(range2))
    return range(min(start1,start2), max(end1, end2)+1)

answer = 0
if len(sys.argv) > 2:
    with open(sys.argv[1], 'r') as ranges, open(sys.argv[2], 'r') as ingredients:
        fresh_list = list()
        ingredient_list = list()
        for line in ranges:
            new_range = list(int(i.strip('\n')) for i in line.split("-"))
            new_range[1] = new_range[1] + 1
            fresh_list.append(range(*new_range))
            fresh_list = sorted(fresh_list, key= lambda x: x[0])

        for ingredient in ingredients:
            ingredient = int(ingredient.strip('\n'))
            for fresh_range in fresh_list:
                if ingredient in fresh_range:
                    answer += 1
                    break

        print(f"{answer=}")

else:
    with open(sys.argv[1], 'r') as ranges:
        fresh_queue = deque()
        for line in ranges:
            new_range = list(int(i.strip('\n')) for i in line.split("-"))
            new_range[1] = new_range[1] + 1
            fresh_queue.append(range(*new_range))
            fresh_queue = deque(sorted(fresh_queue, key= lambda x: x[0]))

        final_ranges = list()
        mod_range = range(0)
        while fresh_queue:
            current_range = fresh_queue.popleft()
            #print(f"\n{mod_range=}\n{current_range=}")
            if is_overlapping(current_range, mod_range):
                mod_range = min_max(current_range, mod_range)

            else:
                final_ranges.append(mod_range)
                answer += len(mod_range)
                mod_range = current_range

        final_ranges.append(mod_range)
        answer += len(mod_range)

        print(answer)
        print(f"\n{final_ranges=}")
