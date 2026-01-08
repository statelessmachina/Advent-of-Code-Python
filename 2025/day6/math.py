#!/usr/bin/env python3

import sys

def main(input_file):
    answer = 0
    with open(input_file, 'r') as input:
        input_array = list(list(line.replace('\n','').rsplit() for line in input))
        number_array = list(list(map(int, input_array[row])) for row in range(len(input_array[:-1])))
        number_array.append(input_array[-1])
        
        
        print(number_array)
        print(list(zip(*number_array)))
        

if __name__ == "__main__":
    main(sys.argv[1])
