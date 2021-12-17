#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    # Write your code here
    lucia = list(a)
    carlos = list(b)
    lucia_score = 0
    carlos_score = 0
    i=0
    final=[]
    while i <=2:
        if lucia[i]>carlos[i]:
            lucia_score+=1
        elif carlos[i]>lucia[i]:
            carlos_score+=1
        else:
            pass
        i+=1
    final.append(lucia_score)
    final.append(carlos_score)
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

