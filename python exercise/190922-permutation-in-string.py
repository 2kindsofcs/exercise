import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Length = len(s1)
        s2Length = len(s2)
        alphabet = string.ascii_lowercase
        s1Letter = [ 0 for _ in range(26) ]
        for letter in s1:
            index = alphabet.index(letter)
            s1Letter[index] += 1
        for i in range(0, s2Length - s1Length + 1):
            s2Letter = [ 0 for _ in range(26) ]
            for j in range(i, i + s1Length):
                index = alphabet.index(s2[j])
                s2Letter[index] += 1
            if s1Letter == s2Letter:
                return True
        return False
        
# 여전히 time limit exceeded
