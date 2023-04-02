from iterables_examples import take, LinkedList
my_list = LinkedList()
my_list.add_to_head(0)
my_list.add_to_tail(42)
my_list.add_to_tail(1)
my_list.add_to_tail(5)

def cycle(iter):
    class Cycle_iterable:
        def __init__(self, init_iter):
            self.iterable = init_iter
            self.iterator = self.iterable.__iter__()
            self.curr = None
        def __next__(self):
            try:
                item = self.iterator.__next__()
                return item
            except StopIteration:
                self.iterator = self.iterable.__iter__()
                return self.iterator.__next__()
        def __iter__(self):
            return self 
    return Cycle_iterable(iter)
cl = cycle([1,2,3])
print(take(cl, 20))
print(take(cycle(my_list), 10))

