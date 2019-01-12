#!/bin/python3
# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    string = "#"
    for i in range (1,n):
        if n == 1:
            break
        else:    
            print(" " * (n-i) + string)
            string += "#"
    print(string)
    return

if __name__ == '__main__':
    n = int(input())

    staircase(n)
