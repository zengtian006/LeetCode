class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, cur=0, head
        while cur:
            count+=1
            cur=cur.next
        if k<=1 or count<k:
            return head
        pre, cur=None, head
        for _ in range(k):
            temp = cur.next
            cur.next=pre
            pre=cur
            cur=temp
        head.next=self.reverseKGroup(cur,k)
        return pre
    
    
    #  1->2->3->4->5  k= 3
    #  1  <-  2  <-  3   |  4  ->   5
    # head          pre    cur
    # head.next = cur
    #. 5<-4<-1<-2<-3
    # reutrn pre