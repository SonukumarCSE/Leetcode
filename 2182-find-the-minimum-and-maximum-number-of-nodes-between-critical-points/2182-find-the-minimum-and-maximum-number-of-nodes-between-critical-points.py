# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return None
        if head.next is None:
            return [-1,-1]
        if head.next.next is None:
            return [-1,-1]
        idx = []
        curr = head.next
        prev = head
        count = 2
        while curr.next is not None:
            if curr.val > prev.val and curr.val > curr.next.val:
                idx.append(count)
            if curr.val < prev.val and curr.val < curr.next.val:
                idx.append(count)
            curr = curr.next
            prev = prev.next
            count += 1
        if len(idx) == 0 or len(idx) == 1:
            return [-1,-1]
        ans = []
        print(idx)
        min_dist = float('inf')
        for i in range(1,len(idx)):
            min_dist = min(min_dist,idx[i]-idx[i-1])
        print(min_dist)
        ans.append(min_dist)
        ans.append(idx[-1]-idx[0])
        
        return ans