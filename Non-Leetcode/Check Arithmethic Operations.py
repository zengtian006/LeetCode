# Example 1:

# Input: "A + ((B) + (C)) = ((B + C) + A)" 
# Output: true
# Example 2:

# Input: "A - (B + C) = -B + (A - C)"
# Output: true
# Example 3:

# Input: "A - (B + C) = B + (A - C)"
# Output: false

class Solution:
    def Operations(self, strr: string) -> int:
        # strr = "A + ((B) + (C)) = ((B + C) + A)" 
        data = strr.split('=')
        s1 =data[0].strip() +'+'
        s2 = data[1].strip() + '+'
        d1 = self.check(s1)
        d2 = self.check(s2)
        for i in [1,-1]:
            v1 = sorted(d1[i])
            v2 = sorted(d2[i])
            if v1!= v2:
                return False
        return True
        
        
    def check(self, strr):
        sign = 1
        char = ""
        dic = collections.defaultdict(list)
        stack = []
        i = 0
        while i<len(strr):
            if strr[i] in '+-)':
                if char:
                    if stack:
                        sign = sign *stack[-1]
                    dic[sign].append(char)
                    char = ""
                sign = 1 if strr[i] == '+' else -1
                if strr[i] == ')':
                    stack.pop()
            if strr[i].isalpha():
                char += strr[i]
            if strr[i] == '(':
                stack.append(sign)
                sign = 1
            i+=1
        return dic