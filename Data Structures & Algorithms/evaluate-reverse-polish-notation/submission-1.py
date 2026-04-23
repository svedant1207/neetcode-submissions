class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stk.append(int(i))
            else:
                b = stk.pop()
                a = stk.pop()

                if i == "+":
                    stk.append(a + b)
                elif i == "-":
                    stk.append(a - b)
                elif i == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(a / b))  # important

        return stk[0]