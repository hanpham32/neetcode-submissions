class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for t in tokens:
            if t in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num2 - num1)
                elif t == "*":
                    stack.append(num1 * num2)
                elif t == "/":
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(t))
        return stack.pop()