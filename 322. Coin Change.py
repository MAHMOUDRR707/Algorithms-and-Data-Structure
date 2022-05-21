import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin = [math.inf]*(amount+1)
        coin[0] = 0
        for i in coins :
            for j in range(i,amount+1):
                coin[j] =  min(coin[j],coin[j-i]+1)
        if coin[-1] ==  math.inf:
            return -1
        return coin[-1]
