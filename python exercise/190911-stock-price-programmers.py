def solution(prices):
    length = len(prices)
    minima, answer = [], []
    for i in range(1, length):
        if prices[i] - prices[i - 1] < 0:
            minima.append(i)
    for i in range(length):
        for index in minima:
            if index > i and prices[i] > prices[index]:
                answer.append(index - i)
                break
        else:
            answer.append(length - i - 1)
    return answer
    
    
# 채점 결과
# 정확성: 66.7
# 효율성: 0.0
# 합계: 66.7 / 100.0
