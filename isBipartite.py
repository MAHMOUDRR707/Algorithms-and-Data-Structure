class Solution:
    def isBipartite(self, graph: List[List[int]]) :
        n =  len(graph)
        z = {}
        for i in range(n):
            if i not in z.keys():
                 z[i] = 1
            q  = [i]
            while q :
                cur =  q.pop(0)
                for j in graph[cur] :
                    if j not in z.keys():
                        z[j] =  -z[cur]
                        q.append(j)
                    elif z[cur] ==  z[j] :
                        return False
        return True
