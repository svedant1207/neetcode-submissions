class Solution:
    def countPrimes(self, n: int) -> int:
        
        def is_prime(n):
            if n <= 1:
                return False

            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False 
            return True

        count = 0

        for i in range(n):
            if is_prime(i) == True:
                count += 1
            else:
                continue
        

        return count
            
            
            
        