import unittest

def findnum(list, num): #연습문제 1. list와 특정 수를 받아서 해당 수와 같은 값을 가지는 요소들의 index를 리스트로 돌려줌
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

if __name__ == '__main__':
        unittest.main()


def findname(numlist, namelist, studentnum): # 연습문제 2. 학생들의 번호와 이름을 각각 리스트로 받고 특정 학생의 이름을 받아서 그 사람의 번호 돌려주기
    n = len(numlist)
    for i in range(n):
        if numlist[i] == studentnum:
            return namelist[i]
    return "?"

numlist = [39, 14, 45, 22]
namelist = ["wolf", "croc", "white", "black"]
#print(findname(numlist,namelist,14))
#print(findname(numlist,namelist,21)) 임의로 테스트를 해볼 수도 있겠지만 unittest를 활용하자!