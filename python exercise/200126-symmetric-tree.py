# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 앞에서 절반까지 읽은 것과 끝에서 절반까지 읽은 것이 동일해야 함
        queue = [root]
        childrenList = []
        while queue:
            element = queue.pop(0)
            if element.left:
                childrenList.append(element.left.val)
            if element.right:
                childrenList.append(element.right.val)
            if not queue:
                length = len(childrenList)
                if length % 2 != 0:
                    return False
                half = length // 2
                latter = childrenList[half:]
                latter.reverse()
                if childrenList[:half] != latter:
                    return False
                # 이렇게 하면 while문을 돌지 못함, 정수들의 리스트니까.
                # 리스트를 하나만 써서 풀 수는 없는 건가?
                queue = childrenList
                childrenList = []
        return True
