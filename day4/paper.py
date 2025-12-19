#!/usr/bin/env python3

import sys

answer = 0 

with open(sys.argv[1], 'r') as input:
    # Grabs first 2 lines to start checking rolls
    # Initializes with one empty row to check top row
    lines = list()
    while len(lines) < 3:
        line = input.readline()
        line = list(line.strip())
        lines.append(line)
    while line:
        line = list(line.strip())
        print(f"{len(line)=}\n{line=}")
        

        line = input.readline()
