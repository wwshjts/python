class Singleton():
    o_ptr = None
    is_inint = False
    def __new__(cls, *args, **kwargs):
        if Singleton.o_ptr:
            return Singleton.o_ptr
        else:
            Singleton.o_ptr = super().__new__(cls)
            return Singleton.o_ptr
    def __init__(cls, *args, **kwargs):
        if not Singleton.is_inint:
            super().__init__(*args, **kwargs)
            Singleton.is_inint = True
        
class Counter:
    def __init__(self, initial_count = 0, step = 1):
        self.count = initial_count
        self.step = step
    def inc(self):
        self.count += self.step

class GlobalCounter(Singleton, Counter):
    pass
c1 = GlobalCounter(initial_count = 1, step = 2)
c2 = GlobalCounter()
c1.inc()
print(c2.count)
print(id(c1) == id(c2))