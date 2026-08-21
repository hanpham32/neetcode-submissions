class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestN = 0
        l, r = 0, 0  #  sliding window method

        set_ = set()
        count = 0
        while r < len(s):
            if s[r] not in set_:
                set_.add(s[r])
                r += 1
                count += 1
            else:
                set_.remove(s[l])
                l += 1
                count -= 1
            
            longestN = max(longestN, count)
        
        return longestN
        