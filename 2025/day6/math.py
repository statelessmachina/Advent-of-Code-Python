#!/usr/bin/env python3

import sys
from math import prod

def collapse_list(iterable: list[int]) -> int:
    if iterable[-1] == '*':
        return prod(iterable[:-1])
    else:
        return sum(iterable[:-1])

def main(input_file):
    answer = 0
    with open(input_file, 'r') as input:
        input_array = list(list(line.replace('\n','').rsplit() for line in input))
        number_array = list(list(map(int, input_array[row])) for row in range(len(input_array[:-1])))
        number_array.append(input_array[-1])
        input_array = list(zip(*number_array))
        
        number_array = list()
        for line in input_array:
            number_array.append(collapse_list(line))

        number_array.append('+')

        return collapse_list(number_array)
        

if __name__ == "__main__":
    print(main(sys.argv[1]))
