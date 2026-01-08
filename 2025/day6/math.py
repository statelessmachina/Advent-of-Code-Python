#!/usr/bin/env python3

import sys
import numpy as np

answer = 0
with open(sys.argv[1], 'r') as input:
    input_array = np.array(list(line.replace('\n','').rsplit() for line in input))
    
    for col in range(len(input_array[0])):
        print(input_array[:,col])
