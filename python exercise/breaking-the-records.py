# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    # 처음엔 min=socre[0], max=score[0]
    # 이후 각 점수가 max보다 큰지 min보다 작은지 체크
    # 해당하면 그 값을 교체
    # 교체할 때마다 각 count +1 
    minScore = maxScore = scores[0]
    minCount = maxCount = 0
    for score in scores:
        if score < minScore:
            minScore = score
            minCount += 1
        elif score > maxScore:
            maxScore = score
            maxCount += 1
    return [maxCount, minCount]

if __name__ == "__main__":
    scoreNum = input()
    scores = list(map(int,input().split()))
    result = ' '.join(map(str, breakingRecords(scores)))
    print(result)