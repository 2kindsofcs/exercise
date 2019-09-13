def solution(n, lost, reserve):
    lostSet = set(lost)
    reserveSet = set(reserve)
    lost = list(lostSet - reserveSet)
    reserve = list(reserveSet - lostSet)
    lost.sort()
    reserve.sort()
    lostLength = len(lost)
    reserveLength = len(reserve)
    indexLost, indexReserve = 0, 0
    count = 0
    while indexLost < lostLength and indexReserve < reserveLength:        
        if reserve[indexReserve] + 1 == lost[indexLost] or reserve[indexReserve] - 1 == lost[indexLost]:
            count += 1
            indexReserve += 1
            indexLost += 1
            continue
        if reserve[indexReserve] > lost[indexLost]:
            indexLost += 1
        else:
            indexReserve += 1
    return n - lostLength + count

# set을 안 쓰고 풀 수는 없을까? 
