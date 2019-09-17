def solution(numbers, target):
    def DFS(index, number):
        if index == len(numbers):
            return 1 if number == target else 0 
        else:
            return DFS(index + 1, number + numbers[index]) + DFS(index + 1, number - numbers[index])
    return DFS(0, 0)
