DPlist = [0, 1]
def fibo(n):
    if n <= len(DPlist) - 1:
        return DPlist[n]
    else:
        DPlist.append(fibo(n-2) + fibo(n-1))
        return DPlist[n]

def zeroAndOne(n):
    if n == 0 :
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo(n-1), fibo(n))

if __name__ == '__main__':
    testcaseNum = int(input().rstrip())
    for i in range(testcaseNum):
        num = int(input())
        zeroAndOne(num)