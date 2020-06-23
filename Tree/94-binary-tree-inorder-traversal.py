from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.stack = list()
        ans = list()
        if root is None:
            return ans
        p = root
        while True:
            self.visit_along_vine(p)
            if len(self.stack) == 0:
                break
            ans.append(self.stack[-1].val)
            p = self.stack[-1].right
            self.stack.pop()
        return ans

    def visit_along_vine(self, p):
        while p:
            self.stack.append(p)
            p = p.left
