import unittest

def insertionSort(list): # 카멜표기법으로 함수 이름 작성
    n = len(list)
    for i in range(1,n):
        value = list[i]
        position = i
        while position > 1 and list[position-1] > value:
            list[position] = list[position-1]
            position -= 1
        list[position] = value      
        yield list

class testInsertionSort(unittest.TestCase):
    def test_1(self):
        list = [5, 24, 11, 35, 13]
        itr = insertionSort(list)

        # sort iterations 
        self.assertEqual(next(itr), [5, 24, 11, 35, 13])
        self.assertEqual(next(itr), [5, 11, 24, 35, 13])
        self.assertEqual(next(itr), [5, 11, 24, 35, 13])
        self.assertEqual(next(itr), [5, 11, 13, 24, 35])
    
        with self.assertRaises(StopIteration):
            next(itr)   

if __name__ == '__main__':
        unittest.main()

