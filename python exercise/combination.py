# 중복된 요소는 없다고 가정 
# 알파벳이나 숫자처럼 정렬 가능한 타입의 요소들로 이루어진 리스트라고 가정 
def combination(numsPicked, M, N):
    if N == 0:
        print(numsPicked)
    start = (numsPicked[-1]+1) if numsPicked else 0
    for i in range(start, M):
        numsPicked.append(i)
        combination(numsPicked, M, N-1)
        numsPicked.pop()

combination([], 3, 2)


