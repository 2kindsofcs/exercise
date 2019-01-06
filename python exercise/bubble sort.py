def bubbleosort(list):
    totalnum = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, totalnum):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        totalnum = totalnum - 1        
    

test = [4,2,7,1,3]
bubbleosort(test)
print(test)




