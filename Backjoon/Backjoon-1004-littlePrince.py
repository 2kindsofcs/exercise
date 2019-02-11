# 백준 1003번 어린왕자 문제
# https://www.acmicpc.net/problem/1004

def isInSystem(x,y,a,b,r): #한 좌표와 원의 중심 좌표, 반지름을 인자로 받아 해당 좌표가 원 안에 있는지 여부를 return
    return (((x - a) ** 2) + ((y - b) ** 2)) < (r ** 2) # return값은 True of False 

testNum = int(input())
for i in range(testNum): 
    x1, y1, x2, y2 = map(int, input().split()) 

    planetNum = int(input()) 
    startSet = set()  # 중복을 허용하지 않는 집합을 이용한다. 
    goalSet = set()
    planetId = 0   # 제일 처음 주어지는 행성계 좌표는 0, 그 다음 좌표는 1... 하는 식으로 고유 숫자를 붙여준다. 
                
    for j in range(planetNum):
        a, b, r = map(int,input().split()) 
        if isInSystem(x1,y1,a,b,r): # 출발점 x1, y1이 해당 행성계 안에 있으면 starSet에 planetId 추가
            startSet.add(planetId)
        if isInSystem(x2,y2,a,b,r): # 마찬가지로 도착점 x2, y2가 해당 행성계 안에 있으면 goalSet에 planetId 추가
            goalSet.add(planetId)
        planetId += 1

    if startSet == goalSet: # 만약 두 집합이 동일하면 가로질러야 할 행성계가 없으므로 0 
        print(0)
    elif startSet & goalSet: # 두 집합에 교집합이 있을 경우 합집합에서 교집합을 제외한 행성계 수만큼 가로질러야 한다.
        print(len((startSet|goalSet) - (startSet&goalSet)))
    else: # 두 집합이 동일하지도 않고 교집합도 없다면 각 집합에 포함된 행성계 갯수만큼 가로질러야 한다. 
        print(len(startSet) + len(goalSet))  
    















