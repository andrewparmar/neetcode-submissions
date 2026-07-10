# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        slow = dummy # d, d, 1, 2, 3
        fast = dummy # d, 1, 2, 3, 4
        prev = None

        counter = 0
        while fast.next:
            fast = fast.next
            counter += 1
            if counter >=n:
                prev = slow
                slow = slow.next

        prev.next = slow.next
        slow.next = None

        return dummy.next
