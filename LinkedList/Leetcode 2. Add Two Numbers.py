class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            sums = 0
            if l1:
                sums += l1.val
                l1 = l1.next
            if l2:
                sums += l2.val
                l2 = l2.next
            sums += carry
            cur.next = ListNode(sums%10)
            cur = cur.next
            carry = sums//10
        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next