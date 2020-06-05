class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap,(lst.val,idx, lst))
            
        dummy = ListNode(0)
        cur = dummy
        while heap:
            v,idx, lst = heapq.heappop(heap)
            cur.next = lst
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val,idx, cur.next))
        return dummy.next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]):
        if not lists:
            return
        n = len(lists)
        if n == 1:
            return lists[0]
        mid = n//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2 .next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next