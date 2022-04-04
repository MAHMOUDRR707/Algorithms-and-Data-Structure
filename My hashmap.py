
class MyHashMap:

    def __init__(self):
        self.l =  {}

    def put(self, key: int, value: int):
        self.l[key] = value

    def get(self, key: int):
        if key not in (self.l.keys()) :
            return -1
        return self.l[key]

    def remove(self, key: int):
        if key in  self.l.keys() :
            del self.l[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
