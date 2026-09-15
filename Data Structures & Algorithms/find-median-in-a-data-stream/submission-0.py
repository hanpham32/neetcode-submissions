class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()

    def findMedian(self) -> float:
        if (len(self.stream) == 1):
            return self.stream[0]
        elif (len(self.stream) % 2 == 0):
            firstNum = self.stream[len(self.stream) // 2 - 1]
            secondNum = self.stream[len(self.stream) // 2]
            return (firstNum + secondNum) / 2
        else:
            return self.stream[len(self.stream) // 2]