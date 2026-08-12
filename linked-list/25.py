from typing import Optional


def hex_val(obj) -> str:
    return hex(id(obj))[-4:]


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

    def x(self):
        t = self
        while t:
            print(t.val, end=" ")
            t = t.next
        print()

    def __repr__(self) -> str:
        return f"(self={hex_val(self)}, val={self.val}, next={hex_val(self.next) if self.next else None})"


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


def get_next_k(cur, k) -> Optional[ListNode]:
    t = cur
    while t and k:
        t = t.next
        k -= 1
    return t


def reverse_ll(head, tail):
    if head == tail:
        return head, tail
    head_, tail_ = reverse_ll(head.next, tail)
    head.next = tail_.next
    tail_.next = head
    return head_, head


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_ll(head, tail):
            if head == tail:
                return head, tail
            head_, tail_ = reverse_ll(head.next, tail)
            head.next = tail_.next
            tail_.next = head
            return head_, head
        dummy = ListNode()
        dummy.next = head
        pre_head = dummy
        tail = get_next_k(head, k - 1)
        while tail:
            rev_head, rev_tail = reverse_ll(head, tail)
            pre_head.next = rev_head
            head = rev_tail.next
            tail = get_next_k(head, k - 1)
            pre_head = rev_tail
        return dummy.next


head = ListNode.build_from_list(range(5))
print_list(head)
head = Solution().reverseKGroup(head, 3)
print_list(head)
