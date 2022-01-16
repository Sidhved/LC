# Definition for singly-linked list.
from async_timeout import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre,tmp=None,None
        while(head):
            tmp=head.next
            head.next=pre
            pre=head
            head=tmp
        return pre