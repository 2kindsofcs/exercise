#!/bin/python3
#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if completion[i] != participant[i]:
            return participant[i] 
    return participant[-1]

# 테스트 케이스 모두 통과.
# sort()를 떠올리느냐 못 떠올리느냐가 관건인 듯.
# 완주하지 못한 사람이 동명이인인지 아닌지 체크해서 그 여부에 따라 각기 다른 조치를 취해야할 것 같지만,
# 잘 따져보면 동명이인이든 아니든 결국 participant의 이름을 return하게 된다.
# 다만 해당 이름이 맨 마지막에 위치할 수도 있다는 점만 놓치지 않으면 된다. 