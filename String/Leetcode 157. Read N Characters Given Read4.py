class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        buf4 = [None]*4
        res = []
        while n > 0:
            k = read4(buf4)
            if not k:
                return idx
            for i in range(min(k,n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx