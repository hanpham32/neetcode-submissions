class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', ']': '[', '}':'{'}

        stack = []

        for c in s:
            if c in closeToOpen:
                if stack:
                    item = stack.pop()
                    print(item)
                    if item != closeToOpen[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True