from iterables_examples import take, LinkedList
my_list = LinkedList()
my_list.add_to_head(0)
my_list.add_to_tail(42)
my_list.add_to_tail(1)
my_list.add_to_tail(5)

def cycle(iter):
    while True:
        yield from iter
cl = cycle([1,2,3])
print(take(cl, 20))
print(take(cycle(my_list), 10))

