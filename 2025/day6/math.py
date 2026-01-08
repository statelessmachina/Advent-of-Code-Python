#!/usr/bin/env python3

import sys


def main(input_file):

    answer = 0
    with open(input_file, 'r') as input:
        input_array = list(list(line.replace('\n','').rsplit() for line in input))
        print(list(zip(*input_array)))
        

if __name__ == "__main__":

    main(sys.argv[1])
