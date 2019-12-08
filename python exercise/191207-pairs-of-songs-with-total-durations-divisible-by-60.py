class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        length = len(time)
        answer = 0
        countList = [0] * 60
        for i in range(length):
            index = time[i] % 60
            answer += countList[(60 - index) % 60]
            countList[index] += 1
        return answer
    
# Runtime: 240 ms, faster than 94.91% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Memory Usage: 16.3 MB, less than 9.09% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Next challenges:
# 문제를 엉뚱하게 풀고 있었다. 오늘 다시 보니 문제가 제대로 이해되었다.
