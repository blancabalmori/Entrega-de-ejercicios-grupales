#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def gameOfStones(n,cont=0):
# Write your code here
    ganador = ''
    if cont%2==0:
        ganador += 'P2'
    else:
        ganador += 'P1'
    if n==0 or n==1:
        return ganador
    else:
        if n%5==0 or n%5==1:
            return gameOfStones(n-5,cont+1)
        elif n%3==0 or n%3==1:
            return gameOfStones(n-3,cont+1)
        elif n%2==0 or n%2==1:
            return gameOfStones(n-2,cont+1)
