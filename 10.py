class LRU_cache:
    def __init__(self, capacity=16):
        self._cache =  dict()
        self._que = []
        self._size = 0
        self._capacity = capacity
        self._time = 0

    def put(self, key, value):
        if self._capacity > self._size:
            self._cache[key] = value  
            self._size += 1
            self._que.append(key)
        else:
            self._cache.pop(self._que.pop(0))
            self._cache[key] = value
            self._que.append(key)
    def get(self, key):
            if key in self._cache:
                #Here is O(n)
                self._que.remove(key)
                self._que.append(key)
                return self._cache[key] 
            return None
    def pr(self):
        print(self._cache)
        print(self._que)
ch = LRU_cache(capacity = 3)
for i in range(5):
    ch.put(str(i), i)
ch.pr()
ch.get('2')
ch.put('w', 42)
ch.pr()