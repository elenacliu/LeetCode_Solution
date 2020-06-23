class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        if i > 0:
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        if i < n - 1:
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
