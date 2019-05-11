# 택시에는 최대 4명이 탈 수 있으며 한 택시에 여러 그룹이 타도 가능. 한 그룹에 속한 사람의 수는 자연수이며 최대 4.

import math

def idealTaxi(s):
    answer = 0
    s.sort()
    count1, count2, count3, count4 = s.count(1), s.count(2), s.count(3), s.count(4)
    if count1 and count3:
        if count1 >= count3:
            answer += count3
            count1 = count1 - count3
            count3 = 0
        elif count3 > count1:
            answer += count1
            count3 = count3 - count1
            count1 = 0         
    answer += count2 // 2
    count2 = count2 % 2 
    if count1 and count2:
        answer += math.ceil((2 + count1) // 4)
        count2 = 0
    answer += count4 + count3 + count2
    return answer

test1 = [1,2,4,4,3,2] # 4
test2 = [1,1,1,4,3,2] # 3
test3 = [4,2,2,2,3] # 4
test4 = [4,3,3,1,3,1,3] # 5
print(idealTaxi(test1))
print(idealTaxi(test2))
print(idealTaxi(test3))
print(idealTaxi(test4))