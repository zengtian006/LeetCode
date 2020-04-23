class Solution:
    def simplifyPath(self, path: str) -> str:
        strs = path.split('/')
        res = []
        for s in strs:
            if s == '..':
                if res:
                    res.pop()
            elif s.isalpha() or (s and s!='.'):
                res.append(s)
        return '/' + '/'.join(res)