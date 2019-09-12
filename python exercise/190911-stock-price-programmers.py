def solution(prices):
    length = len(prices)
    answer = [ length - i - 1 for i in range(length) ]
    for i in range(length - 1):
        for j in range(i + 1, length):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
    return answer

# 채점 결과
# 정확성: 66.7
# 효율성: 33.3
# 합계: 100.0 / 100.0
