def partition(list, start, end):
    pivot = list[end]
    leftpointer = start
    rightpointer = end - 1
    sorted = False
    while not sorted:
        while list[leftpointer] <= pivot and leftpointer <= rightpointer:
            leftpointer += 1
        while list[rightpointer] >= pivot and leftpointer <= rightpointer:
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

testList = [7,2,5,8,11,3,12]
print(quickSort(testList, 0, len(testList)-1))
testList2 = [4,4,1,7,11,23,4]
print(quickSort(testList2, 0, len(testList2)-1))

        