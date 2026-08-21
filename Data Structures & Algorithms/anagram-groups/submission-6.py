class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        for i, s in enumerate(strs):
            charFreq = Counter(s)
            freqMap[tuple(sorted(charFreq.items()))].append(s)
        return [item for key, item in freqMap.items()]