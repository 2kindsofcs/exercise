# 프로그래머스 스택/큐 기능개발 문제
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]

    latest = days.pop(0)
    count = 1
    while days:
        current = days.pop(0)
        if latest >= current:
            count += 1
        else: # latest < current
            answer.append(count)
            count = 1
            latest = current
    answer.append(count)

    return answer

def solution2(progresses, speeds):
    answer = []
    def calcRequiredDays(job_idx):
        return math.ceil((100 - progresses[job_idx]) / speeds[job_idx])

    latest = calcRequiredDays(0)
    count = 1
    for i in range(1, len(progresses)):
        current = calcRequiredDays(i)
        if latest >= current:
            count += 1
        else: # latest < current
            answer.append(count)
            count = 1
            latest = current
    answer.append(count)

    return answer
