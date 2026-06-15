from collections import OrderedDict
from threading import Lock

class LRUCache:
    def __init__(self, capacity: int = 3):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.lock = Lock()

    def get(self, key: str):
        with self.lock:
            if key not in self.cache:
                return None
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: str, value: int):
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)

            self.cache[key] = value

            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
