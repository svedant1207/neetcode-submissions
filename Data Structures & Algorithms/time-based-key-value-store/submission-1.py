class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        
        self.d[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''

        val = self.d[key]

        l, r = 0, len(self.d) -1
        res = ''

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  
                left = mid + 1        
            else:
                right = mid - 1       
                
        return res