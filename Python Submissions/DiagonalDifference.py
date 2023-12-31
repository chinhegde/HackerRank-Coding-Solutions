#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(n,arr):
    
    d1 = sum([arr[i][i] for i in range(n)])
    d2 = sum([arr[i][n-1-i] for i in range(n)])
    
    return abs(d1-d2)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
