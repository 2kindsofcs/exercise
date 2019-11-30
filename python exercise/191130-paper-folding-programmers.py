import copy

def solution(n):
    dic = [[], [0], [0,0,1], [0,0,1,0,0,1,1]]
    length = len(dic)
    if n < length:
        return dic[n]
    start = length
    for i in range(start, n+1):
        result = copy.deepcopy(dic[-1])
        prev = copy.deepcopy(dic[-1])
        prev.reverse()
        result.append(0)
        for bit in prev:
            if bit == 0:
                result.append(1)
            else:
                result.append(0)
        dic.append(result)
    return dic[n]
