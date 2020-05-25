class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cur = [0]*8
        firstDay = []
        count = 0
        while N>0:
            for i in range(1,7):
                if cells[i-1] == cells[i+1]:
                    cur[i] = 1
                else:
                    cur[i] = 0
            if count==0:
                firstDay = cur[:]
            elif cur == firstDay:
                N %= count
                if N == 0:
                    N = count
            count +=1
            N-=1
            cells = cur[:]
        return cur