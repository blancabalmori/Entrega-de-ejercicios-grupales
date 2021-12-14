#!/bin/python3
import math
import os
import random
import re
import sys

def staircase(n):
    while n > 0 :
    contador = n
    segundo_contador = 1
    piramide = []
    espacios_piramide = []
    while contador < n :
        for i in range contador :
            espacios_piramide.append(' ')
        for j in range segundo_contador :
            piramide.append('#')
        contador -= 1
        segundo_contador +=

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)