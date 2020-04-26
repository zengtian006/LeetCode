class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        pre = slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        firstHalf = self.sortList(head)
        secondHalf = self.sortList(slow)
        return self.sort(firstHalf,secondHalf)
    
    def sort(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            elif left.val > right.val:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next