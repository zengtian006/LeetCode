class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1,s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        res = ListNode(0)
        sums =0
        while s1 or s2:
            if s1:
                sums += s1.pop()
            if s2:
                sums += s2.pop()
            res.val = sums%10
            head = ListNode(sums//10)
            head.next = res
            res = head
            sums //= 10
        return res if res.val else res.next