class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        l, r = 0, 0
        N = len(s)
        uniqueChar = set()
        res = 0
        while r < N:
            while r < N and s[r] not in uniqueChar:
                uniqueChar.add(s[r])
                r += 1
            res = max(res, r - l)
            if r >= N:
                break
            while s[l] != s[r]:
                uniqueChar.remove(s[l])
                l += 1
            l += 1
            r += 1
        return res