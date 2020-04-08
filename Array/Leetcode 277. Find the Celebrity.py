class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for i in range(1,n):
            if not knows(i,celebrity):
                celebrity = i
                
        for i in range(n):
            if celebrity !=i and (knows(celebrity,i) or not knows(i, celebrity)):
                return -1
        return celebrity