class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    remove.append(i)
                else:
                    stack.pop()
        remove.extend(stack)
        remove.sort(reverse = True)
        for i in remove:
            s = s[:i]+s[i+1:]
        return s