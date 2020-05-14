class Solution:
    def maxLength(self, arr: List[str]) -> int:
        word_sets = []
        for i in range(len(arr)):
            if len(arr[i])>len(set(arr[i])):
                continue
            s = set()
            for char in arr[i]:
                s.add(char)
            word_sets.append(s)
        
        self.res = 0
        self.helper(word_sets, 0, [])
        return self.res
    
    def helper(self, word_sets, idx, tempList):
        if tempList:
            self.res = max(self.res, len(tempList))
        for i in range(idx, len(word_sets)):
            if not set(tempList) & word_sets[i]:
                self.helper(word_sets, i+1, tempList+list(word_sets[i]))