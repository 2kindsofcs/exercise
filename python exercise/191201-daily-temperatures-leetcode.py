class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        result = [ 0 for _ in range (length) ]
        stack = [0]
        for i in range(1, length):
            while stack: 
                if T[stack[-1]] < T[i]:
                    prevIndex = stack.pop()
                    days = i - prevIndex
                    result[prevIndex] = days
                else:
                    break
            stack.append(i)
        return result
            
        
# Runtime: 512 ms, faster than 84.62% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.4 MB, less than 97.37% of Python3 online submissions for Daily Temperatures.

# 조금만 생각하면 쉬운데, 복잡하게 생각해서 못 풀던 문제.
            
