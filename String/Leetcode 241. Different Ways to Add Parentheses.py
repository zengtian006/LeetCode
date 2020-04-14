class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == "+":
                            res.append(l+r)
                        elif input[i] == "-":
                            res.append(l-r)
                        elif input[i] == "*":
                            res.append(l*r)
        
        if not res:
            return [int(input)]
        return res