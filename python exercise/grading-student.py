# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade <= 37 or grade == 100: # 사실 100은 맨 마지막에 포함됨
            result.append(grade)
        elif grade % 5 == 3:
            result.append(grade+2)
        elif grade % 5 == 4:
            result.append(grade+1)
        else:
            result.append(grade)
    return result 
    # 37 이하거나 100이면 그대로 둠 
    #아닐 경우 5로 나눠서 나머지가 3이거나 4면 +2 또는 +1

def gradingStudents2(grades):
    result = []
    for grade in grades:
        if grade > 37:
            remain = grade % 5
            if remain > 2:
                # 0 1 2 3 4 5
                # 0 1 2 3 4 0
                # 5 4 3 2 1 5
                grade = grade + 5 - remain
        result.append(grade)
    return result

def gradingStudents3(grades):
    return [
        ((x + 2) // 5) * 5
            if (x > 37 and x % 5 > 2)
            else x
                for x in grades
    ]



