#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    print("Inserta la posición inicial y la final de la casa: ")
    s,t = map(int, input().strip().split(' '))
    print("Inserta la posición del manzano y del naranjo: ")
    a,b = map(int, input().strip().split(' '))
    print("Inserta a la distancia a la que caen las manzanas del manzano y las naranjas del naranjo: ")
    m,n = map(int, input().strip().split(' '))
    print("Inserta las distancias que hay entre cada par de manzanas: ")
    apple = list(map(int, input().strip().split(' ')))
    print("Inserta las distancias que hay entre cada par de naranjas: ")
    orange = list(map(int, input().strip().split(' ')))

    manzanascaidas = sum([1 for f in apple if (f+a) >= s and (f+a) <= t])
    naranjascaidas = sum([1 for f in orange if (f+b) >= s and (f+b) <= t])
    
    if manzanascaidas != 1:
        print ("Han caído: "+ str(manzanascaidas) + " manzanas en la casa")
    else:
        print ("Han caído: "+ str(manzanascaidas) + " manzana en la casa")
    if naranjascaidas != 1:   
        print ("Han caído: "+ str(naranjascaidas) + " naranjas en la casa")
    else:
        print ("Han caído: "+ str(naranjascaidas) + " naranjas en la casa")
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)