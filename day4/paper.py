#!/usr/bin/env python3

import sys

answer = 0 

with open(sys.argv[1], 'r') as input:
    # Grabs first 2 lines to start checking rolls
    # Initializes with one empty row to check top row
    line = list((input.readline()).strip())
    lines = list()
    lines.append(list('.' * len(line)))

    while len(lines) < 3:
        lines.append(line)
        line = list((input.readline()).strip())

    while line:
        print(f"{lines}")
        lines = lines[1:]
        lines.append(line)
        line = list((input.readline()).strip())
