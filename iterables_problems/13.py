from iterables_examples import take, LinkedList
def chain(*args):
    class Chain_iterable:
        def __init__(self, args):
            self.iterable_list = args 
            self.n = len(args) - 1
            self.cnt = 0
            self.iterator = (self.iterable_list[self.cnt]).__iter__()
            self.curr = None
        def __next__(self):
            try:
                item = self.iterator.__next__()
                return item
            except StopIteration:
                if self.cnt < self.n:
                    self.cnt += 1
                    self.iterator = self.iterable_list[self.cnt].__iter__()
                    return self.iterator.__next__()
                raise StopIteration
        def __iter__(self):
            return self

    return Chain_iterable(args)

my_list = LinkedList()
my_list.add_to_head(0)
my_list.add_to_tail(42)
my_list.add_to_tail(1)
my_list.add_to_tail(5)

ch = chain([1,2,3], my_list, [4,5,6])

for item in ch:
    print(item, end = ' ')