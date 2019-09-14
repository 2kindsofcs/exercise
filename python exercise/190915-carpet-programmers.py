import math
def solution(brown, red):
    redL = int(math.sqrt(red))
    while True:
        if red % redL == 0:
            break
        redL = redL - 1
    candidate = []
    for i in range(1, redL + 1):
        if red % i == 0:
            redW = red // i 
        candidate.append([redW, i])
    for cand in candidate:
        if (cand[0] * 2) + (cand[1] * 2) + 4 == brown:
            return [cand[0] + 2, cand[1] + 2]
