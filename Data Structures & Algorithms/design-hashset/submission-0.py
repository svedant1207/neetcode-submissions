class MyHashSet:

    def __init__(self):
        self.leng = 1000
        self.buckets = [[] for i in range(self.leng)]
        
    def add(self, key: int) -> None:
        hash_s = 0
        hash_s = key % self.leng

        if key not in self.buckets[hash_s]:
            self.buckets[hash_s].append(key)


    def remove(self, key: int) -> None:
        hash_s = 0
        hash_s = key % self.leng

        if key in self.buckets[hash_s]:
            self.buckets[hash_s].remove(key)
        

    def contains(self, key: int) -> bool:
        hash_s = 0
        hash_s = key % self.leng

        return key in self.buckets[hash_s]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)