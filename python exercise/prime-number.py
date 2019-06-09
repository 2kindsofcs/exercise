# 소수 개수 구하기 문제.
# 인풋은 2이상 , 1은 소수가 아님 --> 최소 정답은 1, none이 들어올 일은 없음.

def solution(n):
    primeList = [2]
    for i in range(1, n+1):
        for num in primeList:
            if num ** 2 <= i and i % num != 0:
                primeList.append(i)
            else:
                pass
    return len(primeList)

print(solution(10))


