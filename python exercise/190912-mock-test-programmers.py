def solution(answers):
    if not answers:
        return []
    pattern1 = [1,2,3,4,5] 
    pattern2 = [2,1,2,3,2,4,2,5] 
    pattern3 = [3,3,1,1,2,2,4,4,5,5]  
    length = len(answers)
    answer1 = [ 0 for _ in range(length) ] 
    answer2 = [ 0 for _ in range(length) ]
    answer3 = [ 0 for _ in range(length) ]
    index = 0
    index1, index2, index3 = 0, 0, 0
    while index < length:
        answer1[index] = pattern1[index1]
        answer2[index] = pattern2[index2]
        answer3[index] = pattern3[index3]
        index1 += 1
        index2 += 1
        index3 += 1
        if index1 == 5:
            index1 = 0
        if index2 == 8:
            index2 = 0
        if index3 == 10:
            index3 = 0
        index += 1
    score1, score2, score3 = 0, 0, 0
    for i in range(length):
        if answers[i] == answer1[i]:
            score1 += 1
        if answers[i] == answer2[i]:
            score2 += 1
        if answers[i] == answer3[i]:
            score3 += 1
    result = []
    maxScore = max(score1, score2, score3)
    if maxScore == score1:
        result.append(1)
    if maxScore == score2:
        result.append(2)
    if maxScore == score3:
        result.append(3)
    return result
    
# 너무 반복되는 부분이 많은 것 같은데, 이게 정말 최선인가?
