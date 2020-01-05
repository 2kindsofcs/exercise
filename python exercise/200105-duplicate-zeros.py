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
        for i in range(endIndex):
            if arr[i] == 0:
                # in-place로 해야하는데...
        
