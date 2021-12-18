#!/bin/python3
import math
import os
import random
import re
import sys

#Complete the 'gradingStudents' function below.
#The function is expected to return an INTEGER_ARRAY.
#The function accepts INTEGER_ARRAY grades as parameter

def gradingStudents(grades):
    calificaciones = list(map(int,input("Inserte calificaciones: ").split()))
    notasfinales = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= 0 and calificaciones[i] <= 100:
            if calificaciones[i] >= 40:
                if calificaciones[i]%5 == 3: 
                    calificaciones[i] += 2
                elif calificaciones[i]%5 ==4:
                    calificaciones[i] += 1
                notasfinales.append(calificaciones[i])
            else:
                notasfinales.append(calificaciones[i])
            
        else:
            print("Has introducido notas incorrectas")
    print("Las notas finales son: "+ str(notasfinales))
gradingStudents()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
result = gradingStudents(grades)
fptr.write('\n'.join(map(str, result)))
fptr.write('\n')
fptr.close()