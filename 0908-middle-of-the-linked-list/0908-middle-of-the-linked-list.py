# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        tmp = head

        while head:
            head = head.next
            length += 1
        
        length = length // 2 + 1

        while length > 1:
            tmp = tmp.next
            length -= 1

        return tmp

    
        