from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # remove least recently used

# Example
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))  # 10
lru.put(3, 30)     # removes key 2
print(lru.get(2))  # -1