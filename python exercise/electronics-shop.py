# https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, b):
    sumList = []
    if min(keyboards) + min(drives) > b:
        print(-1)
    for keyboard in keyboards:
        for drive in drives:
            sumList.append(keyboard + drive)
    result = max(filter(lambda x: x <= b, sumList))
    print(result)

if __name__ == "__main__":
    b, n, m = map(int,input().split())
    keyboards = list(map(int,input().split()))
    drives = list(map(int,input().split()))
    getMoneySpent(keyboards, drives, b)

