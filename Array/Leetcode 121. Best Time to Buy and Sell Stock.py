class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_buy = float('inf')
        max_profit = 0
        for p in prices:
            min_buy = min(min_buy,p)
            max_profit = max(max_profit, p-min_buy)
        return max_profit

# 求极值，考虑DP
# 计算前面最小的buy price，再用当前数字减去最小的buy price