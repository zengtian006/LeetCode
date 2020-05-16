class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        w1 = max(A,E)
        w2 = min(C,G)
        width =max(0, w2-w1) 
        
        h1 = max(B,F)
        h2 = min(D,H)
        height = max(0, h2-h1)
        
        a1 = (C-A)*(D-B)
        a2 = (G-E)*(H-F)
        return a1+a2-width*height