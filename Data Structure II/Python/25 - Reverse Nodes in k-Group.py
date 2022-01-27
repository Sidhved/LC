# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = ListNode(0)
        p.next = head
        head = p
        q = p
        while True:
            i = 0
            while i < k and q != None:
                q = q.next
                i = i + 1
            if q == None:
                return head.next
            while p.next != q:
                tmp1 = p.next
                tmp2 = q.next
                p.next = p.next.next
                q.next = tmp1
                q.next.next = tmp2
                
            for j in range(k):
                p = p.next
            q = p
            
        return head.next