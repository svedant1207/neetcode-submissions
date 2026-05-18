class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        def count(n):
            c = 0
            mask = 1

            for i in range(64):
                c += n & (mask << i) != 0

            return c

        for i in range(n+1):
            output.append(count(i))

        
        return output


        

                