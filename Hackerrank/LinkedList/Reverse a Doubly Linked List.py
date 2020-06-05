def reverse(head):
    cur = head
    pre = None
    while cur:
        nxt = cur.next
        cur.next = pre
        cur.pre = nxt

        pre = cur
        cur = nxt
    return pre