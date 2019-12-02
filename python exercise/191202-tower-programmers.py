def solution(heights):
    length = len(heights)
    answer = [ 0 for _ in range(length) ]
    stack = []
    index = length - 1
    while index >= 0:
        while stack:
            if heights[stack[-1]] < heights[index]:
                prev = stack.pop()
                answer[prev] = index + 1
            else:
                break
        stack.append(index)
        index = index - 1
    return answer
