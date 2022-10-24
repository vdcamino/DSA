class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        for start, end, weight in times:
            adj_list[start].append((weight, end))

        distances = [+inf] * (n + 1)
        distances[0], distances[k] = 0, 0

        min_heap = [(0, k)]
        heapq.heapify(min_heap)

        while min_heap:
            cur_weight, cur_node = heapq.heappop(min_heap)

            for next_weight, next_node in adj_list[cur_node]:
                if cur_weight + next_weight < distances[next_node]:
                    distances[next_node] = cur_weight + next_weight
                    heapq.heappush(min_heap, (distances[next_node], next_node))

        return max(distances) if max(distances) != +inf else -1
