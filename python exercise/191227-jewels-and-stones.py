class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for letter in S:
            if letter in J:
                count += 1
        return count
        
        
# Runtime: 28 ms, faster than 86.05% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
# 좋아요가 엄청 많은 문제여서 호기심에 풀었는데, 굉장히 쉬운 문제여서 조금 당황했다. 
