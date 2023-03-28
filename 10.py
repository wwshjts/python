class LRU_cache:
    def __init__(self, capacity=16):
        self.__cache =  dict()
        self.__que = []
        self._size = 0
        self._capacity = capacity
        self._time = 0

    def put(self, key, value):
        if self._capacity > self._size:
            self.__cache[key] = value  
            self._size += 1
            self.__que.append(key)
        else:
            self.__cache.pop(self.__que.pop(0))
            self.__cache[key] = value
            self.__que.append(key)
    def get(self, key):
            if key in self.__cache:
                #Here is O(n)
                self.__que.remove(key)
                self.__que.append(key)
                return self.__cache[key] 
            return None
    def pr(self):
        print(self.__cache)
        print(self.__que)

ch = LRU_cache(capacity = 3)
for i in range(5):
    ch.put(str(i), i)
ch.pr()
ch.get('2')
ch.put('w', 42)
ch.pr()