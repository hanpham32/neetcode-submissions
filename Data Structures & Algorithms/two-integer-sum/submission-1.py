class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in diffMap:
                return [diffMap[diff], i]
            else:
                diffMap[n] = i
        return []