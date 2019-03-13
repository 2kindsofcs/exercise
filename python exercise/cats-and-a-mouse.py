# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen

def catAndMouse(x, y, z):
    catAtoZ = abs(x-z)
    catBtoZ = abs(y-z)
    if catBtoZ > catAtoZ:
        print("Cat A")
    elif catAtoZ > catBtoZ:
        print("Cat B")
    # else:
    #     print("Mouse C")
    print("Mouse C")
    
if __name__ == "__main__":
    testNum = int(input())
    for i in range(testNum):
        x,y,z = map(int, input().split())
        catAndMouse(x, y, z)

