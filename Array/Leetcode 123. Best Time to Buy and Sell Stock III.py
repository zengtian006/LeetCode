class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1: return 0
        min_buy = prices[0]
        dp_left, dp_right = [0]*n, [0]*n
        for i in range(1,n):
            min_buy = min(min_buy, prices[i])
            dp_left[i] = max(dp_left[i-1], prices[i] - min_buy)
        
        max_sell = prices[-1]
        for i in range(n-2, -1, -1):
            max_sell = max(max_sell, prices[i])
            dp_right[i] = max(max_sell - prices[i], dp_right[i-1])
        
        res = 0
        for x, y in zip(dp_left,dp_right):
            res = max(res, x+y)
        return res

# 求极值，考虑DP
# 分别从左(1,n-1) 右(n-2,0)计算最大profit
# 比如 [a,b,c,d,e,f,g,h,i], 以e为分割点，e之前最大profit看dp_left。 e之后最大profit看dp_right. 