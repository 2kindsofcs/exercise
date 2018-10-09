# 1부터 100까지 출력
for i in range (1,101):
    print(i)

# 5의 배수의 총합
sum = 0
for i in range (1,1001):
    if i % 5 == 0:
        sum += i 
print(sum)

# 리스트 내 정수형 평균 구하기
A = [70, 65, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0 
for i in A:
    sum += i 
print(sum/len(A))

# 혈액형 별 학생수 합계 
bloodtype = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
numforbloodtype = {}
for i in bloodtype:
    if i in numforbloodtype:
        numforbloodtype[i] +=1
    else:
        numforbloodtype[i] = 1
print(numforbloodtype)
 
 # 리스트내포 연습 1: 5의 배수를 2배 해서 리스트로 따로 빼기
numbers = [1,2,3,4,5]
result = [i * 2 for i in numbers if i % 2 == 1]
print(result)

# 리스트내포 연습 2: 문장에서 모음 제거하기
# 꽤나 헤맸는데, join을 쓸 거라는 생각 자체를 못했다
# 전반적으로 공부를 하면서 많이 느끼는 건데, 마치 콜럼부스의 달걀 같다는 생각이 많이 든다.
# 한번 떠올리면 몹시 쉽지만, 떠올리기 전까지는 안개 속에 쌓여있는 것 같다.
string = "Life is too short, you need python"
vowels = 'aeiou'
print(''.join([i for i in string if i not in vowels]))
