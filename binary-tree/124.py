from typing import List, Optional

null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def build_from_list(cls, li: List) -> Optional["TreeNode"]:
        for i, e in enumerate(li):
            if e is None:
                continue
            li[i] = cls(e)
            if i == 0:
                continue
            parent = i - 1
            parent //= 2
            if i % 2:
                li[parent].left = li[i]
            else:
                li[parent].right = li[i]
        return li[0]


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1010

        def dfs(node: Optional[TreeNode]):
            nonlocal ans
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(0, left)
            right = max(0, right)
            ret = node.val + left + right
            ans = max(ans, ret)
            return node.val + max(left, right)

        dfs(root)
        return ans


li = [-10, 9, 20, null, null, 15, 7]
root = TreeNode.build_from_list(li)
s = Solution()
ret = s.maxPathSum(root)
print(ret)
