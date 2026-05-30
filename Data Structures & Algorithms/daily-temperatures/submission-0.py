class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0] * len(t)
        stk = []

        for i, tem in enumerate(t):

            while stk and tem > t[stk[-1]]:
                prev = stk.pop()
                res[prev] = i - prev  
            stk.append(i)

        return res
            


        