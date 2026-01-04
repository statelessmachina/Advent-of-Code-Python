#!/usr/bin/env python3

import sys
import numpy as np

answer = 0
with open(sys.argv[1], 'r') as input:
    input_array = list(list(line.replace('\n',' ') for line in input))
    print(input_array)
