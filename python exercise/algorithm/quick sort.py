def partition(list, start, end):
    pivot = list[end]
    leftpointer = start
    rightpointer = end - 1
    sorted = False
    while not sorted:
        while list[leftpointer] < pivot and leftpointer < rightpointer:
            leftpointer += 1
        while list[rightpointer] > pivot and leftpointer < rightpointer:
            rightpointer -= 1
        if leftpointer >= rightpointer:
           sorted = True
        else: 
            list[leftpointer], list[rightpointer] = list[rightpointer], list[leftpointer]
    list[leftpointer], list[end] = list[end], list[leftpointer]
    return leftpointer

def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot-1)
        quickSort(list, pivot+1, end)
    return list

testList = [7,2,5,12,8,11,3]
quickSort(testList, 0, len(testList)-1)
print(testList) # it prints [2,3,5,7,8,12,11]. there must be somthing wrong.
        
    