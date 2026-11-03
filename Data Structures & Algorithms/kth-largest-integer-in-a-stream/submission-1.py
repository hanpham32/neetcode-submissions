class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
# 1, 2, 3, 3
# 1, 2, 3, 3, 3
# 1, 2, 3, 3, 3, 5
# 1, 2, 3, 3, 3, 5, 6
# 1, 2, 3, 3, 3, 5, 6, 7
# 1, 2, 3, 3, 3, 5, 6, 7, 8

# 3rd
# 2, 4, 5, 8
# 2, 3, 4, 5, 8