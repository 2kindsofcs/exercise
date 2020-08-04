# 대여 / 반납이 가능하고 쓸 수 있는 게 없으면 최대 수량이 아니면 새로 생성. 최대를 초과해야하면 그냥 실패.
import unittest

class Obj:
    def __init__(self):
        pass

class ObjectPool:
    def __init__(self, initialCount, maxCount, objectFactory):
        self.freeObjects = []
        self.objectFactory = objectFactory
        self.maxCount = maxCount
        for _ in range(initialCount): 
            self.freeObjects.append(objectFactory())
        self.usedObejcts = []

    def getInstance(self):
        if self.freeObjects:
            obj = self.freeObjects.pop()
            self.usedObejcts.append(obj)
            return obj
        else:
            length = len(self.usedObejcts)
            if length < self.maxCount:
                self.freeObjects.append(self.objectFactory())
                return self.getInstance()
            else:
                return None
                
    def returnInstance(self, obj):
        self.freeObjects.append(obj)
        index = self.usedObejcts.index(obj)
        del self.usedObejcts[index]

class TestObjectPool(unittest.TestCase):
    def test_basic_usage(self):
        pool = ObjectPool(3, 5, Obj)

        some_obj = pool.getInstance()
        self.assertIsNotNone(some_obj)
        # use some_obj as much as wanted.
        pool.returnInstance(some_obj)

    def test_starve(self):
        pool = ObjectPool(3,5, Obj)

        some_obj0 = pool.getInstance()
        self.assertIsNotNone(some_obj0)

        some_obj1 = pool.getInstance()
        self.assertIsNotNone(some_obj1)

        some_obj2 = pool.getInstance()
        self.assertIsNotNone(some_obj2)

        some_obj3 = pool.getInstance()
        self.assertIsNotNone(some_obj3)

        pool.returnInstance(some_obj0)
        pool.returnInstance(some_obj1)
        pool.returnInstance(some_obj2)
        pool.returnInstance(some_obj3)

if __name__ == '__main__':
    unittest.main()