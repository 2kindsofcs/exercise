class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        count = 0
        endIndex = 0
        for i in range(length):
            if count >= length:
                endIndex = i 
                break
            add = 1
            if arr[i] == 0:
                add = 2
            count += add
        modified = []
        for i in range(endIndex):
            modified.append(arr[i])
            if arr[i] == 0:
                modified.append(0)
        if modified:
            for i in range(length):
                arr[i] = modified[i]
                
# Runtime: 64 ms, faster than 93.12% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
# 이게 정말 문제 의도대로 푼 게 맞는건가?
# 출제자는 다른 메모리를 할당해서 쓰는 걸 원하지 않았을 것 같은데...
