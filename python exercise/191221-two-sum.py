class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDic = {}
        for i, num in enumerate(nums):
            indexDic[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if num == diff:
                continue
            if diff in indexDic:
                result = [i, indexDic[diff]]
                result.sort()
                return result
            
 # 쉬워보여서 머리풀겸 선택한 문제인데, 보기보다는 조금 더 생각할 게 많은 듯. 다시 풀어봐야겠다.
