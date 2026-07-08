class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append((stack.pop() + stack.pop()))
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append((stack.pop() * stack.pop()))
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                if a == 0:
                    stack.append(0)  # Or handle this scenario as needed for your algorithm
                else:
                    stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
