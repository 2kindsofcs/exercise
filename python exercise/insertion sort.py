import unittest

def insertionSort(list): # 카멜표기법으로 함수 이름 작성
    n = len(list)
    for i in range(1,n):  # 1번째 요소(list[0])를 기준으로 2번째 요소(list[1])부터 비교 시작
        value = list[i]
        position = i
        while position > 1 and list[position-1] > value: # value보다 작은 값을 가진 위치에 도달하면 while문을 빠져나간다
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