class Solution:
    
    def __init__(self):
        self.q = collections.deque()
        
    def read(self, buf: List[str], n: int) -> int:
        idx = 0
        while len(self.q) and n>0:
            buf[idx] = self.q.popleft()
            n -= 1
            idx += 1
        
        while n > 0:
            buf4 = [None]*4
            k = read4(buf4)
            if not k:
                return idx
            if k>n:
                self.q.extend(buf4[n:k])
            for i in range(min(k,n)):
                buf[idx] = buf4[i]
                idx+=1
                n-=1
        return idx