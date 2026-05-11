class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        total = 0

        for i in tokens:
            if i.isalnum():
                stk.append(int(i))
            else:
                a = stk.pop()
                if i == "+":
                    total = stk[-1] + a
                    stk.append(total)
                elif i == "-":
                    total = stk[-1] - a
                    stk.append(total)
                elif i == "*":
                    total = stk[-1] * a
                    stk.append(total)
                else:
                    total = stk[-1] // a
                    stk.append(total)

        return total

                
        