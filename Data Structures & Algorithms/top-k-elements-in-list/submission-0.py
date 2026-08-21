class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for item, v in freq.items():
            heapq.heappush(heap, (-v, item))
        return [heapq.heappop(heap)[1] for i in range(k)]