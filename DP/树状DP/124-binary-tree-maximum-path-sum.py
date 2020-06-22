# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        val = -0x3f3f3f3f

        def solve(root):
            if root is None:
                return 0

            left = max(0, solve(root.left))
            right = max(0, solve(root.right))
            lmr = left + right + root.val
            # Python闭包只能修改可变类型，不能修改不可变类型
            # 必须指明val是非局部变量
            nonlocal val
            val = max(val, lmr, max(left, right) + root.val)
            # 为什么不返回max(lmr, max(left, right) + root.val)呢？是因为返回的肯定只能是经过root的单边路径
            # 这样才能组成新的路径
            return root.val + max(left, right)

        solve(root)
        return int(val)
