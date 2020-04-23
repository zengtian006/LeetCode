class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s : return NestedInteger()
        if s[0] != '[' : return NestedInteger(int(s))
        stack = []
        start = 0
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
                start = i+1
            elif s[i] in ',]':
                if s[start:i].lstrip('-').isdigit(): #judge if it's negative number
                    num = int(s[start:i])
                    stack[-1].add(NestedInteger(num))
                if s[i] == ']':
                    ni = stack.pop()
                    if stack:
                        stack[-1].add(ni)
                    else:
                        return ni
                start = i+1