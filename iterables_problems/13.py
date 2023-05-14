from iterables_examples import take, LinkedList
def chain(*args):
    for it in args:
        yield from it

my_list = LinkedList()
my_list.add_to_head(0)
my_list.add_to_tail(42)
my_list.add_to_tail(1)
my_list.add_to_tail(5)

ch = chain([1,2,3], my_list, [4,5,6])

for item in ch:
    print(item, end = ' ')
print()