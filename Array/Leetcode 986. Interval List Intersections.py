class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i<len(A) and j<len(B):
            left = max(A[i][0],B[j][0])
            right = min(A[i][1], B[j][1])
            if left<=right:
                interval = [left, right]
                res.append(interval)

            if B[j][1]>A[i][1]:
                i+=1
            else:
                j+=1
        return res