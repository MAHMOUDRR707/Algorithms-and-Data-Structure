class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        x = 1 
        right =[1]
        left = [1]
        rate =  ratings[::-1]
        for i in range(1,n):
            if ratings[i-1] > ratings[i] : 
                right.append(1)
            elif ratings[i-1] == ratings[i] :
                right.append(1)
            else : 
                right.append(right[i-1]+1)
        for i in range(1,n):
            if rate[i-1]  > rate[i] : 
                left.append(1)
            elif rate[i- 1] == rate[i] :
                left.append(1)
            else : 
                left.append(left[i-1]+1)
        total = [0] *n
        for i in range(n):
            total[i] = max(left[n-1-i],right[i])
        return(sum(total))
