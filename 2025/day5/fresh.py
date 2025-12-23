#!/usr/bin/env python3

import sys

answer = 0
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

