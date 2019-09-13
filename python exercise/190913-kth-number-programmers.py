def solution(array, commands):
    answer = []
    for command in commands:
        listToCheck = array[command[0] - 1:command[1]]
        listToCheck.sort()
        answer.append(listToCheck[command[2] - 1])
    return answer
