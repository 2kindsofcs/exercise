import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)
        if s1Length > s2Length:
            return False
        alphabet = string.ascii_lowercase
        s1Letter = [ 0 for _ in range(26) ]
        s2Letter = [ 0 for _ in range(26) ]
        for letter in s1:
            index = alphabet.index(letter)
            s1Letter[index] += 1
        for i in range(s1Length):
            index = alphabet.index(s2[i])
            s2Letter[index] += 1
        for i in range(0, s2Length - s1Length):
            if s1Letter == s2Letter:
                return True
            # 중복되는 부분은 검사하지 않고, 범위에서 벗어난 1글자의 빈도를 제거하고
            # 새로 조사하는 1글자의 빈도에 + 1 해준다.
            s2Letter[alphabet.index(s2[i])] -= 1
            index = alphabet.index(s2[i + s1Length])
            s2Letter[index] += 1
        return s1Letter == s2Letter 
        # s1: "a", s2: "a" 같은 경우 range(0,0)이 되어 코드가 아예 실행되지 않음
        # 따라서 return False가 아니라 s1Letter == s2Letter라고 하면 의도대로 동작하면서
        # 예외처리 코드를 따로 작성하지 않아도 됨. 

# Runtime: 76 ms, faster than 64.72% of Python3 online submissions for Permutation in String.
# Memory Usage: 13.6 MB, less than 8.33% of Python3 online submissions for Permutation in String.
                
            
