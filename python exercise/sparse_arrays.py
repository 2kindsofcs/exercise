#!/bin/python3
# https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    return [strings.count(query) for query in queries]
    # 조금만 더 생각하면, list comprehension에는 식이 들어갈 수 있으므로 계산한 식으로 바로 끝낼 수 있으면
    # 굳이 중간 변수를 넣을 필요는 없다. 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()