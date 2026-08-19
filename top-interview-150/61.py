# Definition for singly-linked list.
from typing import Optional


def hex_val(obj) -> str:
    return hex(id(obj))[-4:]


def print_list(t: Optional[ListNode]):
    if not t:
        print("<empty>")
        return
    ret = ""
    while t.next:
        ret += f"{t.val} -> "
        t = t.next
    ret += f"{t.val}"
    print(ret)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build_from_list(cls, li) -> Optional["ListNode"]:
        if not li:
            return None
        dummy = cls()
        t = dummy
        for n in li:
            t.next = cls(n)
            t = t.next
        return dummy.next

    def __repr__(self) -> str:
        return f"(self={hex_val(self)}, val={self.val}, next={hex_val(self.next) if self.next else None})"


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        length = 0
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        length += 1
        k = k % length
        if k == 0:
            return head
        cur.next = head
        new_head_pre_step = length - k
        new_head_pre_step -= 1
        cur = head
        while new_head_pre_step:
            cur = cur.next
            new_head_pre_step -= 1
        new_head_pre = cur
        new_head = new_head_pre.next
        # print(new_head_pre, new_head)
        new_head_pre.next = None
        return new_head


head = ListNode.build_from_list(range(1, 6))
print_list(head)
new_head = Solution().rotateRight(head, 2)
print_list(new_head)

for k in range(1,5):
    head = ListNode.build_from_list(range(3))
    # print_list(head)
    new_head = Solution().rotateRight(head, k)
    print_list(new_head)
