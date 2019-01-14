#미완성, 검증 필요

def mergeSort(list):
    n = len(list)

    if n <= 1:
        return list

    halfnum = n // 2
    index = 0 
    group1 = mergeSort(list[0:halfnum])
    group2 = mergeSort(list[halfnum:n])

    while group1 and group2:
        if group1[0] < group2[0]:
            list[index] = group1[0]
            group1.pop(0)
        elif group2[0] < group1[0]:
            list[index] = group2[0]
            group2.pop(0)
        index += 1     

    if group1: 
        list[n-len(group1):] = group1

    if group2:
        list[n-len(group2):] = group2
    
    return list

a = [6,9,2,4,5]
print(mergeSort(a))
