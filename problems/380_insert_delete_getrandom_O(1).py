class RandomizedSet:
    def __init__(self):
        self.data = {}

    def insert(self, val: int) -> bool:
        if self.data.get(val, False):
            return False
        else:
            self.data[val] = True
            return True
    
    def remove(self, val: int) -> bool:
        if self.data.get(val, False):
            self.data.pop(val)
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        idx = 0
        rand_idx = random.randint(0, len(self.data)-1)
        return list(self.data.keys())[rand_idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

