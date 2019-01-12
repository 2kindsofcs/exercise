#!/bin/python3
# https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.

# "#"과 공백의 총합은 언제나 n개이다. 또한 "#"이라는 스트링을 별도로 가공할 필요가 없으므로, 굳이 변수를 선언하지 않아도 된다.
def staircase(n): 
    for i in range (1,n+1):
        print(" " * (n-i) + "#" * i) 

if __name__ == '__main__':
    n = int(input())

    staircase(n)
