class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                return True
        return False

# Runtime: 132 ms, faster than 42.29% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 17.8 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
