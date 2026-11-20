class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # closest to target will be in the front
        stack = [] # arrival time of each fleet
        for pos, spd in cars:
            t = (target - pos) / spd # calc. the arrival time
            if not stack or t > stack[-1]:
                stack.append(t) # create a new fleet
        return len(stack)