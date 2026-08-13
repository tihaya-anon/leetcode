# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 100_010
        prev = None

        def dfs(cur):
            nonlocal ans, prev
            if cur is None:
                return
            dfs(cur.left)
            if prev is not None:
                ans = min(ans, cur.val - prev)
            prev = cur.val
            dfs(cur.right)

        dfs(root)
        return ans
