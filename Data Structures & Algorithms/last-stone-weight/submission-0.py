class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []
        for s in stones:
            maxHeap.append(s * -1)
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:

            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)
            
            new = s1 - s2
            heapq.heappush(maxHeap, new * -1)


        return -maxHeap[0] if maxHeap else 0
