#!/bin/python3
#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    for name in participant:
        partinum = participant.count(name)
        complenum = completion.count(name)
        if partinum != complenum:
            return name

# 정확성 테스트는 모두 통과, 효율성 테스트는 모두 통과하지 못함 
