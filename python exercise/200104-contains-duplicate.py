class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        listLength = len(nums)
        setLength = len(set(nums))
        if setLength < listLength:
            return True
        return False
    
# Runtime: 120 ms, faster than 93.86% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
# set을 쓰는 게 더 비용이 비쌀 줄 알았는데 더 빠르다. 
