class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s,0,len(s)-1)
        i = j = 0
        while j < len(s):
            if s[j] == ' ':
                self.reverse(s,i,j-1)
                i = j+1
            j+=1
        self.reverse(s,i,j-1)
        
    def reverse(self, s, left, right):
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1