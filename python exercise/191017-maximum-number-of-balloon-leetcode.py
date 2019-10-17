class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # b:1, a:1, n:1,  l:2, o:2,
        letterDic = {"b":0, "a":0, "n":0, "l":0, "o":0}
        for letter in text:
            if letter in letterDic:
                letterDic[letter] += 1
        crit1, crit2 = False, False
        minOne = min(letterDic["b"], letterDic["a"], letterDic["n"])
        key = ""
        for letter in letterDic:
            if letterDic[letter] == minOne:
                key = letter
                break
        if letterDic[key] <= letterDic["a"] and letterDic[key] <= letterDic["n"] and letterDic[key] <= letterDic["b"]:
            return min((letterDic["l"] // 2, letterDic["o"] // 2))
        return 0
            
        
# 뭔가 깔끔한 로직이 있을 것 같은데 잘 떠오르질 않는다. 
