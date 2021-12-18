#!/bin/python3
import math
import os
import random
import re
import sys

def staircase(n):
    i=1
    while i<=n:
        print(i*'#')
        i+=1

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)