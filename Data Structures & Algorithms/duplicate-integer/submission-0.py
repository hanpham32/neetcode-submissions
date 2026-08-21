class Solution:
    """
    time: O(n) bc we only iterate through the list once
    space: O(n) worst case we add all items in nums into myset
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        for n in nums:
            if n not in myset:
                myset.add(n)
            else:
                # n is a duplicate
                return True
        
        return False 