#!/usr/bin/env python3

import sys
import numpy as np

answer = 0 
with open(sys.argv[1], 'r') as input:
    line_array = np.array(list(list(line.strip()) for line in input))
    row_len, col_len = line_array.shape

    for i in range(row_len):
        for j in range(col_len):
            
            if line_array[i][j] == '@':
                start_row = 0
                end_row = 0
                start_col = 0
                end_col = 0

                # Assign row indices for sub-matrices
                if i == 0:
                    start_row = i
                else:
                    start_row = i-1

                if i < row_len-2:
                    end_row = i+2
                else:
                    end_row = None

                # Assign column indices for sub-matrices
                if j == 0:
                    start_col = j
                else:
                    start_col = j-1

                if j < col_len-2:
                    end_col = j+2
                else:
                    end_col = None

                sub_matrix = line_array[start_row:end_row,start_col:end_col]

                unique,count = np.unique(sub_matrix,return_counts=True)
                count -= 1
                counts = dict(zip(unique,count))

                if '@' in counts: 
                   if counts['@'] < 4:
                       answer += 1

print(f"{answer=}")
