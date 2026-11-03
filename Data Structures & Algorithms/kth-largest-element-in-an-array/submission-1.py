class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        ans = 0
        for _ in range(k):
            ans = heapq.heappop(heap) * -1
        return ans