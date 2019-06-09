# 정수 배열이 주어지고, 해당 배열 내 정수의 평균값 구하기
def solution(arr):
    length = len(arr)
    sum = 0 
    for i in range(length):
        sum += arr[i]
    answer = sum / length
    return answer

# 2016년 1월 1일은 금요일, 2016년은 윤년이며, a월 b일에 해당하는 a,b가 주어졌을 때 무슨 요일인지 구하기
def solution(a, b):
    monthDays = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = sum(monthDays[0:a]) + b - 1
    answer = day[days % 7]
    return answer