# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a,b):
    # 범위는 max(a) 이상~ min(b) 이하
    # a로 나누었을 때 나머지가 0이어야 하며
    # b"를" 나누었을 때 나머지가 0이어야 한다 
    # 해당 숫자들을 리턴하는 것이 아니라, 해당 숫자들의 "수"
    maxA = max(a)
    minB = min(b)
    count = 0
    for num in range(maxA, minB+1):
        if all(num % numA == 0 for numA in a) and all(numB % num == 0 for numB in b):
            count += 1
    return count

if __name__ == "__main__":
    aLen, bLen = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = getTotalX(a, b)
    print(result)








