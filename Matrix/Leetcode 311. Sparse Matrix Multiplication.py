class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m_a, n_a = len(A), len(A[0])
        m_b, n_b = len(B), len(B[0])
        res = [[0]*n_b for _ in range(m_a)]
        for i in range(m_a):
            for j in range(n_a):
                if A[i][j] != 0:
                    for c in range(n_b):
                        res[i][c] += A[i][j]*B[j][c]
        return res