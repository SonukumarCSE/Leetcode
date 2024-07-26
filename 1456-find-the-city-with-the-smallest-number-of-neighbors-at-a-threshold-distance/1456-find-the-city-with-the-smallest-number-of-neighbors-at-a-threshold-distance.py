class Solution:
    def dijikstra(self,adj,x,n):
        distance = [float('inf')] * n
        distance[x] = 0
        minHeap = [(0,x)]

        while minHeap:
            dist,node = heapq.heappop(minHeap)

            if dist > distance[node]:
                continue
            for v,weight in adj[node]:
                new_wt = weight + dist
                if new_wt < distance[v]:
                    distance[v] = new_wt
                    heapq.heappush(minHeap,(new_wt,v))
        return distance
    def findTheCity(self, n: int, edges: List[List[int]], th: int) -> int:
        adj = {i: [] for i in range(n)} 
        for x in edges:
            adj[x[0]].append([x[1], x[2]])
            adj[x[1]].append([x[0], x[2]])
        city_count = float('inf')
        best_city = -1
        for x in range(n):
            temp = self.dijikstra(adj,x,n)
            sum = 0
            for y in temp:
                if y <= th:
                    sum += 1
            sum -= 1
            print(temp)
            print(sum)
            total_city = sum
            if city_count > total_city:
                city_count = total_city
                best_city = x
            elif city_count == total_city:
                best_city = max(best_city,x)
        return best_city