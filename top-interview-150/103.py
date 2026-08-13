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


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue

        if not root:
            return []
        queue = Queue()
        queue.put((root, 0))
        gets = []
        max_level = 0
        while not queue.empty():
            node, level = queue.get()
            max_level = max(max_level, level)
            gets.append((node.val, level))
            if node.left is not None:
                queue.put((node.left, level + 1))
            if node.right is not None:
                queue.put((node.right, level + 1))
        ret = [[] for _ in range(max_level + 1)]
        for node, level in gets:
            ret[level].append(node)
        for i, _ in enumerate(ret):
            if i % 2 == 1:
                ret[i].reverse()
        return ret


root = TreeNode.build_from_list([3, 9, 20, null, null, 15, 7])
ret = Solution().zigzagLevelOrder(root)
print(ret)
