from heapq import heappush, heappop, heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        - Use minimum heap (priority queue)
        - for each list in lists, add all nodes to the priority queue
        - using dummy node, construct a new linked-list by poping from min-heap

        time: o(k*m)
        space: o(k*m)
        """
        min_heap = []
        heapify(min_heap)

        # stack 
        index = 0
        for node in lists:
            curr = node
            while curr:
                heappush(min_heap, (curr.val, index, curr))
                curr = curr.next
                index += 1
        
        dummy = ListNode(None, None)
        curr = dummy 
        while len(min_heap):
            _, _, node = heappop(min_heap)
            curr.next = node
            curr = curr.next
        
        return dummy.next
        