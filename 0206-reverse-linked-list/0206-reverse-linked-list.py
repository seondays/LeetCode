# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        setting = None
        result = ListNode()

        while head:
            tmp = head.next
            head.next = setting
            setting = head
            head = tmp
        
        result.next = setting
        return result.next