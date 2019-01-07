#https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr): 
    dicforratio = {"plus":0, "minus":0, "zero":0} #경우의 수가 3가지이므로 리스트를 써도 상관없었지만 코드를 보다 명확하게 이해할 수 있도록 + 확장성 고려(기초연습문제니까 그럴 일은 없지만)해서 딕셔너리 이용
    for num in arr:
        if num > 0:
            dicforratio["plus"] += 1
        elif num < 0:
            dicforratio["minus"] += 1
        else:
            dicforratio["zero"] += 1           
    for value in dicforratio.values(): # 이 부분에서 꽤 시간을 허비했는데, 처음엔 map을 잘 알지도 못하면서 map과 lambda와 round를 쓰려고 했다가, 결과값이 정수일경우 소수점 아래 여섯번째까지 보여주질 않아서 고민했다. 어쨌든 문제에서는 print되기만을 요구하고 있으므로 결과값이 반드시 숫자여야만 하는 것은 아니기에, format함수를 이용하여 처리하였다.
        print("{0:0.6f}".format(value/len(arr)))           

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)