class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        else:
            self.index_map[val] = len(self.values)
            self.values.append(val)
            return True
    
    def remove(self, val: int) -> bool:
        if val in self.index_map:
            idx = self.index_map[val]
            del self.index_map[val]
            last_val = self.values.pop()
            if idx != len(self.values):
                self.values[idx] = last_val
                self.index_map[self.values[idx]] = idx
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        rand_idx = random.randint(0, len(self.values)-1)
        return self.values[rand_idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
