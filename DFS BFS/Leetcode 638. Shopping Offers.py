class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.helper(price, special, needs, {})
    
    def helper(self,price, special, needs, visited):
        if tuple(needs) in visited:
            return visited[tuple(needs)]
        sums = 0
        for i in range(len(needs)):
            sums += needs[i]*price[i]
        res = sums
        for spec in special:
            needs_copy = needs[::]
            isValid = True
            for i in range(len(needs)):
                if needs_copy[i] < spec[i]:
                    isValid = False
                    break
                needs_copy[i] -= spec[i]
                    
            if isValid:
                res = min(res, spec[-1] + self.helper(price, special, needs_copy,visited))
        visited[tuple(needs)] = res
        return res
