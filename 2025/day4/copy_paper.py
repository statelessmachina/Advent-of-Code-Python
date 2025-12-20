#!/usr/bin/env python3

import sys
import itertools as it

answer = 0 
with open(sys.argv[1], 'r') as input:
    lines = list(line.strip() for line in input)
    
    paper_roll_context = []
    for row_i in len(lines):
        for column_i in len(lines[row_i]):

