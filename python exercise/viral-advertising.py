# https://www.hackerrank.com/challenges/strange-advertising/problem


def viralAdvertising(n):
    totalNumLike = [2]
    totalNumLikeLen = len(totalNumLike)
    if n <= totalNumLikeLen:
        return totalNumLike[n-1]
    for i in range(totalNumLikeLen-1, n-1):
        totalNum = math.floor(totalNumLike[i] * 3 / 2)
        totalNumLike.append(totalNum)
    return sum(totalNumLike)

def viralAdv(n):
    c = 2
    L = 2
    for i in range(1, n):
        L = math.floor(L * 3 / 2)
        c += L
    return c

# L1 = 2
# L(i+1) = floor(L(i) * 3 / 2)
# sum(L, 1, n)

# 메모리가 꼭 이 데이터..etc를 들고 있어야하는가? 그럼으로써 얻는 충분한 이득이 있는가? (ex: 속도 향상)
