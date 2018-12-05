import math

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
min = 0
max = len(prime) - 1

print(prime)
target = int(input("리스트 안의 소수 중 1개를 입력해주세요: "))
guess = 0 
while True:
    guess = math.floor((max + min)/2)
    print("guess는 {0}입니다.".format(guess))
    if max < min:
        print("target이 array에 존재하지 않습니다.")
    elif prime[guess] < target:
        min = guess + 1
        print("min = guess + 1 합니다.")
        continue
    elif prime[guess] > target:
        max = guess - 1
        print("max = guess - 1 합니다.")
        continue
    else:
        print("타겟은 {0}입니다.".format(target))
        break
    
        

