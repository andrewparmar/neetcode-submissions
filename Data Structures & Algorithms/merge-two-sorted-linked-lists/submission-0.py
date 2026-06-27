# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, None)

        curr = dummy

        next1 = list1
        next2 = list2

        while (next1 and next2):
            if next1.val <= next2.val:
                curr.next = next1
                next1 = next1.next
            else:
                curr.next = next2
                next2 = next2.next
            curr = curr.next

        if not next1:
            curr.next = next2
        if not next2:
            curr.next = next1

        return dummy.next

