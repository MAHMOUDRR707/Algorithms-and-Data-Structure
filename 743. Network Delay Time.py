 class Solution:
     def solution():
        graph = defaultdict(list)
        cur_node = {}
        for i in times :
            graph[i[0]].append((i[1],i[2]))
        
        temp =  k 
        visited = set()
        heap =  [(0,k)]
        while heap:
            max_cost,node =  heapq.heappop(heap)
            visited.add(node)
            if len(visited) == n :
                return max_cost
            
            for cost in graph[node]:
                    if cost[0] not in visited :
                        #heap.append((cost[1] + max_cost,cost[0]))
                        heapq.heappush(heap, (cost[1] + max_cost,cost[0]))

        return -1
