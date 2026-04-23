class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        t = row * col
        l = 0
        r = t - 1

        while l <= r:
            mid = (l+r)//2
            i = mid//col
            j = mid % col
            val = matrix[i][j]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid -1
        return False