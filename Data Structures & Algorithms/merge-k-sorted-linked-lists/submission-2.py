from heapq import heapify, heappop, heappush
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapify(min_heap)
        index = 0
        for head in lists:
            curr = head
            while curr:
                heappush(min_heap, (curr.val, index, curr))
                index += 1
                curr = curr.next

        dummy = ListNode(None, None)
        curr = dummy
        while len(min_heap):
            curr.next = heappop(min_heap)[2]
            curr = curr.next
        
        return dummy.next
