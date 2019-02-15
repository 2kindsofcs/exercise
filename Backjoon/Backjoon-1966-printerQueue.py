# 백준 1966번 프린터 큐 문제
# https://www.acmicpc.net/problem/1966

if __name__ == "__main__":
    testNum = int(input())
    for i in range(testNum):
        totalNum, indexGiven = map(int,input().split())
        numList = list(map(int,input().split()))
        positionList = [0 for i in range(totalNum)]
        positionList[indexGiven] = 1 
        count = 0

        while True:
            if numList[0] == max(numList):
                count += 1
                if positionList[0] == 1:
                    print(count)
                    break
                else:
                    numList.pop(0)
                    positionList.pop(0)
            else:
                numList.append(numList.pop(0))
                positionList.append(positionList.pop(0))
