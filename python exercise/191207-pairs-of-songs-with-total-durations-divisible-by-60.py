class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        length = len(time)
        for i in range(length):
            time[i] = time[i] % 60
        count = 0
        for i in range(length-1):
            for j in range(i+1, length):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count 
        
# time limit exceeded
