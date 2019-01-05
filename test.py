def findnum(list, num):
    n = len(list)
    result = []
    for i in range(n):
        if list[i] == num:
            result.append(i)
    return result    
        
testlist = [23,54,64,23]
#print(findnum(testlist,23))

def findname(numlist, namelist, studentnum):
    n = len(numlist)
    for i in range(n):
        if numlist[i] == studentnum:
            return namelist[i]
    return "?"

numlist = [39, 14, 45, 22]
namelist = ["wolf", "croc", "white", "black"]
#print(findname(numlist,namelist,14))
#print(findname(numlist,namelist,21))


def selectionsort(list):
    n = len(list)
    minindex = 0
    for i in range(n-1):
        minindex = i
        # find min element in (i~n)
        for j in range(i+1, n):
            if list[minindex] > list[j]:
                minindex = j
        # do swap!
        list[i], list[minindex] = list[minindex], list[i]
        print("swap {} with {}".format(i, minindex))
        print(list)
            

a = [35, 24, 11, 5]

print(a)
selectionsort(a)

