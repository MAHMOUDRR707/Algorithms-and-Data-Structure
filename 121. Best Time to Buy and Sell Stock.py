#link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#time:o(n)
class Solution:
    def maxProfit(self, prices):
        p =0
        min_p = prices[0]
        x,max_x =0,0
        for i in  prices:
            min_p = min(min_p,i)
            x = i -min_p
            max_x = max(x,max_x)

        return max_x
        
