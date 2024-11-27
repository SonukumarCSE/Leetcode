from typing import List
from collections import deque, defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with direct edges
        mapi = defaultdict(list)
        for i in range(n - 1):
            mapi[i].append(i + 1)

        # Function to find the shortest path using BFS
        def bfs() -> int:
            distances = [-1] * n
            queue = deque([(0, 0)])  # (node, distance)
            distances[0] = 0

            while queue:
                node, dist = queue.popleft()

                for neighbor in mapi[node]:
                    if distances[neighbor] == -1:  # Not visited
                        distances[neighbor] = dist + 1
                        queue.append((neighbor, dist + 1))
                        if neighbor == n - 1:
                            return dist + 1

            return -1

        # Process each query and find the shortest distance from 0 to n-1
        result = []
        for query in queries:
            u, v = query
            mapi[u].append(v)
            result.append(bfs())

        return result

