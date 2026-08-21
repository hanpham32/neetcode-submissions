class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charS = defaultdict(int)
        charT = defaultdict(int)
        for i in range(len(s)):
            charS[s[i]] += 1
            charT[t[i]] += 1
        for num, ctn in charS.items():
            if charS[num] != charT[num]:
                return False
        return True