class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            anagramMap[tuple(charCount)].append(s)
        print(anagramMap)
        return [item for i, item in anagramMap.items()]