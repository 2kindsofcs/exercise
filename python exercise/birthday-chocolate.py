# https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    totalLength = len(s)
    count = 0
    for i in range(totalLength-m+1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

if __name__ == "__main__":
    sLength = input()
    s = list(map(int, input().split()))
    d, m = map(int, input().split())
    print(birthday(s, d, m))



