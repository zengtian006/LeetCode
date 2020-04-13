class Solution:
    writePos = readPos = 0
    buf4 = [' ']*4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        for i in range(n):
            if self.writePos == self.readPos:
                self.writePos = read4(self.buf4)
                self.readPos =0
                if self.writePos == 0:
                    return i
            buf[i] = self.buf4[self.readPos]
            self.readPos += 1
        return n