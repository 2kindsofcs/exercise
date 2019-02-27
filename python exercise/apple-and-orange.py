# https://www.hackerrank.com/challenges/apple-and-orange/problem

if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    appleD = list(map(int, input().split()))
    orangeD = list(map(int,input().split()))
    apples = [apple for apple in appleD if (apple + a) >=s and (apple + a) <=t]
    oranges = [orange for orange in orangeD if (orange + b) >=s and (orange + b)<=t]
    print(len(apples), len(oranges), sep='\n')

    




