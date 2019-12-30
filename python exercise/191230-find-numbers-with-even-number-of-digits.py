class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
    
    
# Runtime: 48 ms, faster than 91.13% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
# 이게 최선인가? num이 크기가 작을 땐 괜찮을지 몰라도 조금만 커져도 str 비용이 비싸서 안 될 텐데.
