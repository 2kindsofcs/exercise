import unittest

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
