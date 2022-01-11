# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        count = 0
        
        fast = head
        while fast != None:
            fast = fast.next
            count += 1
        
        mid = count // 2 + 1
        
        slow = head
        for i in range(1, mid):
            slow = slow.next
            
        return slow