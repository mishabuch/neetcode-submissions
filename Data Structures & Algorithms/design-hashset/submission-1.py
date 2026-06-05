class MyHashSet:

    def __init__(self):
        self.hashsetList = []
        

    def add(self, key: int) -> None:
        if key not in self.hashsetList:
            self.hashsetList.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hashsetList:
            self.hashsetList.remove(key)

    def contains(self, key: int) -> bool:
        if key not in self.hashsetList:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)