# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            if one is None:
                one = headB
            else:
                one = one.next
            
            if two is None:
                two = headA
            else:
                two = two.next
        
        return one