#Stack
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:return head
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        k = k%len(stack)
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while k>0:
            last = stack.pop()
            last.next = cur.next
            cur.next = last
            k -= 1
        stack[-1].next = None
        return dummy.next

# Two pointer       
class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:return head
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        k = k% len(stack)
        
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        fast = slow.next
        slow.next = None
        return fast
        
       
#LinkList 从后往前的算法有两种，一个是快慢指针，一个是Stack