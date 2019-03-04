import math

def kangaroo(x1, v1, x2, v2):
    xDiff = x2-x1  
    vDiff = v1-v2
    if vDiff <= 0:
        return("NO")         
    if (xDiff % vDiff) == 0:
        return("YES")
    return("NO")

def kangaroo(x1, v1, x2, v2):
    xDiff = x2-x1  
    vDiff = v1-v2
    jumpNum = xDiff / vDiff
    if jumpNum == 0:
        print("YES")
    elif vDiff > 0 and jumpNum == math.floor(jumpNum):
        print("YES")
    else:
        print("NO")

def kangaroo2(x1, v1, x2, v2):
    xDiff = x2-x1  
    vDiff = v1-v2
    if vDiff > 0 and vDiff <= xDiff:
        print("YES")
    else:
        print("NO")



# x1, v1, x2, v2 = map(int, input().split())
# kangaroo(x1, v1, x2, v2)

# 0, 3, 4, 2
# 4 / 1 = 4 

# x1 + v1N = x2 + v1N


# v1N = x2 - x1 + v2N
# v1N - v2N = x2-x1
# N(v1-v2) = x2-x1 