import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1length = len(s1)
        if s1length > len(s2):
            return False
        if s1 in s2:
            return True
        s1List = []
        for letter in s1:
            s1List.append(letter)
        permuList = list(map(''.join, itertools.permutations(s1List)))
        for permu in permuList:
            if permu in s2:
                return True
        return False
        
# time limit exceeded
