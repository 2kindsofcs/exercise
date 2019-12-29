import string

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = string.ascii_letters
        result = []
        stack = []
        for letter in S:
            if letter in letters:
                result.append(0)
                stack.append(letter)
            else:
                result.append(letter)
        length = len(S)
        for i in range(length):
            if result[i] == 0:
                result[i] = stack.pop()
        return ''.join(result)
        
        
# Runtime: 28 ms, faster than 85.34% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.
# 뭔가 마음에 안 드는데... 반복문을 딱 한 번만 돌릴 수는 없는 건가?
