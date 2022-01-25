# Definition for singly-linked list.
from async_timeout import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        pre, cur = temp, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val;
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return temp.next