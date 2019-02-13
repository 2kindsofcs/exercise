factoList = [1]
def facto(n):
    global factoList
    if n <= len(factoList):
        return factoList[n-1]
    else:
        factoList.append(facto(n-1)*n)
        return factoList[n-1]

def howManyCase(N, M):
    if N == M:
        print(1)
    else:
        diff = M - N 
        print(int(facto(M)/(facto(N)*facto(diff))))


if __name__ == "__main__":
    testNum = int(input())
    for i in range(testNum):
        N, M = map(int,input().split())
        howManyCase(N, M)

    