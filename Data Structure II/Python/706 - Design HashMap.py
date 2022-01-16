class MyHashMap:

    def __init__(self):
        self.hash_table = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.hash_table[key] = value

    def get(self, key: int) -> int:
        return self.hash_table[key]# return value directly 

    def remove(self, key: int) -> None:
        self.hash_table[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)