#백준 1002번 터렛 문제
#https://www.acmicpc.net/problem/1002

import math
import sys

def whereIsRyu(numbers):
    x1, y1, r1, x2, y2, r2 = map(int, numbers.rstrip().split())
    distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2) 
    sumOfr1r2 = r1 + r2
    difOfr1r2 = abs(r1-r2)
    if distance == 0: # 1)두 사람의 위치가 같고
        if r1 == r2:  # 2)적까지의 거리가 동일하다면 적이 위치할 수 있는 좌표는 무한하다
            print(-1)
        else: # 2)적까지의 거리가 동일하지 않다면 0을 return. else의 중요성이 드러난다. r1>r2, r1=r2, r1<r2 상관없는 것이 포인트.  
            print(0)
    else: # 두 사람의 위치가 같지 않은 경우들
        if distance == sumOfr1r2 or difOfr1r2 == distance: # 밖에서 접하거나 안에서 접하는 경우
            print(1)
        elif distance > sumOfr1r2 or difOfr1r2 > distance: # 두 원이 떨어져 있거나, 한 원이 다른 원 안에 있는 경우 
            print(0)
        else: # 역시 else의 중요성을 확인할 수 있다. 위 두 경우 제외하면 접점이 2개라는 거다. 
              # 예를 들어, distance < sumOfr1r2가 참일 때 접점이 2개지만 이 판단은 모든 경우를 커버하지 못하며,
              # difOfr1r2 > distance를 만족시킬 수도 있다. 
            print(2)

if __name__ == '__main__':
    testcaseNum = int(input().rstrip())
    for i in range(testcaseNum):
        numbers = input()
        whereIsRyu(numbers)