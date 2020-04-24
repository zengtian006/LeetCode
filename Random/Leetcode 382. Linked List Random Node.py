class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        cur = self.head
        count = 0
        res = -1
        while cur:
            count += 1
            if random.randint(1, count) == 1:
                res = cur.val
            cur = cur.next
        return res