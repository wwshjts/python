class Singleton():
    o_ptr = None
    def __new__(cls, *args, **kwargs):
        if Singleton.o_ptr:
            return Singleton.o_ptr
        else:
            Singleton.o_ptr = object.__new__(cls, *args, **kwargs)
            return Singleton.o_ptr
        
class Counter:
    def __init__(self, initial_coun = 0, step = 1):
        self.count = initial_coun
        self.step = step
    def inc(self):
        self.count += self.step

class GlobalCounter(Singleton, Counter):
    pass

c1 = GlobalCounter()
c2 = GlobalCounter()

if (id(c1) == id(c2)):
    print('Im win!')