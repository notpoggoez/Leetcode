import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        heap = []
        for x, y in points:
            d = sqrt(x**2 + y**2)
            heap.append((d, (x,y)))
        
        heapq.heapify(heap)
        while k > 0:
            dist, coord = heapq.heappop(heap)
            res.append(coord)
            k -=1 
        
        return res 