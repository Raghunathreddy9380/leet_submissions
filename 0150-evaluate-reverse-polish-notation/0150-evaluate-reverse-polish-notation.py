class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        Stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = Stack.pop()
                a = Stack.pop()

                if token == "+":
                    Stack.append(a + b)
                elif token == "-":
                    Stack.append(a - b)
                elif token == "*":
                    Stack.append(a * b)
                elif token == "/":
                    Stack.append(int(a / b))
            else:
                Stack.append(int(token))
                
        return Stack[0]