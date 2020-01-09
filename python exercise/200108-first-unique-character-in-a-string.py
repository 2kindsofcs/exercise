import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        indexList = [ -1 for _ in range(26) ]
        alphabets = string.ascii_lowercase
        length = len(s)
        for i in range(length):
            index = alphabets.find(s[i])
            if indexList[index] == -1:
                indexList[index] = i
            else:
                indexList[index] = -2
        characterList = []
        for index in indexList:
            if index != -2 and index != -1:
                characterList.append(index)
        if characterList:
            return min(characterList)
        return -1
        
# Runtime: 176 ms, faster than 16.08% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
# 속도는 다른 사람들보다 훨씬 느린데 메모리는 훨씬 적게 사용한다.
# -1과 -2를 쓰는 게 뭔가 찝찝하다...
