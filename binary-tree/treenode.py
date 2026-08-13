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