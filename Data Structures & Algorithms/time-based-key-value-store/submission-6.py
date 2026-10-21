class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        return

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        li = self.timeMap.get(key, [])
        l, r = 0, len(li) - 1
        while l <= r:
            mid = (l + r) // 2
            if li[mid][0] <= timestamp:
                res = li[mid][1] # valid candidate; continue search
                l = mid + 1
            else:
                r = mid - 1
        return res