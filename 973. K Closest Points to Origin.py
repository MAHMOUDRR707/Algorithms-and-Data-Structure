class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n =  len(points)
        res = {}
        for i in range(n):
            x,y =  points[i]
            z =  (x**2+y**2)**0.5
            res[i] = [z,[x,y]]
        res = dict(sorted(res.items(),key = lambda x:x[1][0])) 
        #print(res)
        result =  list(res.values())
        res = []
        for i in result :
            res.append(i[1])
        return res[:k]
