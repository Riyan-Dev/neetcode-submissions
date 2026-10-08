class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for p in points:
            x1 = p[0]
            x2 = p[1]
            distance = (x1 ** 2) + (x2 ** 2)
            minHeap.append([distance, x1, x2])
        
        heapq.heapify(minHeap)
        
        res = []

        for _ in range(k):
            point = heapq.heappop(minHeap)
            res.append([point[1], point[2]])

        return res
