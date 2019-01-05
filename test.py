import unittest

def findnum(list, num):
    n = len(list)
    result = []
    for i in range(n):
        if list[i] == num:
            result.append(i)
        yield result
    yield result    

class TestFindNum(unittest.TestCase):
    def test_1(self):
        a = [23, 54, 64, 23]

        itr = findnum(a, 23)

        self.assertEqual(next(itr), [0])
        self.assertEqual(next(itr), [0])
        self.assertEqual(next(itr), [0])
        self.assertEqual(next(itr),[0,3])

        self.assertEqual(next(itr),[0,3])

        with self.assertRaises(StopIteration):
            next(itr)

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
        yield list
        # print("swap {} with {}".format(i, minindex))
        # print(list)
    yield list
            
class TestSelectionSort(unittest.TestCase):
    def test_1(self):
        a = [35, 24, 11, 5]

        itr = selectionsort(a)
        # sort iterations
        self.assertEqual(next(itr), [5, 24, 11, 35])
        self.assertEqual(next(itr), [5, 11, 24, 35])
        self.assertEqual(next(itr), [5, 11, 24, 35])

        # result
        self.assertEqual(next(itr), [5, 11, 24, 35])
        # 
        with self.assertRaises(StopIteration):
            next(itr)

if __name__ == '__main__':
        unittest.main()
