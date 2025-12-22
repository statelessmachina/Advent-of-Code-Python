#!/usr/bin/env python3

import sys
import numpy as np

def find_rolls(input_array: np.array) -> tuple([np.array, int]):
    eligible_rolls = 0
    row_len, col_len = input_array.shape

    for i in range(row_len):
        for j in range(col_len):
            
            if input_array[i][j] == '@':
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

                sub_matrix = input_array[start_row:end_row,start_col:end_col]

                # Count '@' and 'X' representing rolls 
                surrounding_rolls = np.count_nonzero(sub_matrix == '@')-1
                surrounding_rolls += np.count_nonzero(sub_matrix == 'X')
                
                if surrounding_rolls < 4:
                    eligible_rolls += 1
                    input_array[i][j] = np.str_('X')

    return (input_array, eligible_rolls)
    

answer = 0 
with open(sys.argv[1], 'r') as input:
    line_array = np.array(list(list(line.strip()) for line in input))
    next_array, eligible = find_rolls(line_array)
    answer = eligible

print(f"{next_array}\n{answer=}")
