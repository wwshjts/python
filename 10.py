class LRU_cache:
    def __init__(self, capacity=16):
        self.__cache = dict()
        self.__que = []
        self.__size = 0
        self.__capacity = capacity
        self.__time = 0

    def put(self, key, value):
        #теперь случай с существующим ключем обрабатывается
        if key not in self.__cache:
            if self.__capacity > self.__size:
                self.__cache[key] = value  
                self.__size += 1
                self.__que.append(key)
            else:
                self.__cache.pop(self.__que.pop(0))
                self.__cache[key] = value
                self.__que.append(key)
        else:
            self.__cache[key] = value
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
    def getsize(self):
        return self.__size

ch = LRU_cache(capacity = 3)
for i in range(5):
    ch.put(str(i), i)
ch.get('2')
ch.put('w', 42)
ch.pr()
print(ch.getsize())
ch.put('w', 1000 - 7)
print(ch.getsize())
ch.pr()