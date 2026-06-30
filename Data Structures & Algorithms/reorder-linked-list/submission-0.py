# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def print_list(head):
            res = []
            curr = head
            while curr:
                res.append(curr.val)
                curr = curr.next
            print(res)

        print("head")
        print_list(head)

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("slow")
        print_list(slow) 
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        print("reversed list")
        print_list(prev) 
        
        curr1 = head
        curr2 = prev
        dummy = ListNode(None, None)
        curr = dummy

        while curr2:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

        if curr1:
            curr.next = curr1
        # return dummy.next
