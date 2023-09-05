# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

# Two Pointer

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
# Hashtable approach

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = {}
        p = head
        while p and p.next:
            if p.next not in visited_nodes:
                visited_nodes[p] = 1
                p = p.next
            else:
                return True
        return False