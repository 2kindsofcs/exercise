def solution(n, words):
    length = len(words)
    answer = [0, 0]
    for i in range(1, length):
        if words[i-1][-1] != words[i][0] or words.count(words[i]) > 2:
            # answer[0] = ?
            # answer[1] = ?
            break
    return answer 
    
    
# 야근을 하고 집에 들어와서인지 간단한 문제인 것 같은데 쉽게 풀리질 않는다.
# 내일 맑은 정신으로 다시 풀어봐야겠다. 
