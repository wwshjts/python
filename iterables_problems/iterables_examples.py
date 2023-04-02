def take(seq, n):
    res = []
    for i in range(n):
        res.append(next(seq))
    return res

class LinkedList:
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt
    def __init__(self):
        self.head = self.tail = None
    def add_to_head(self, val):
        new_head = LinkedList.Node(val, nxt = self.head)
        self.head = new_head
        if not self.tail:
            self.tail = self.head
    
    def add_to_tail(self, val):
        node = LinkedList.Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
    def __iter__(self):
        return LinkedList.Iterator(self)

    class Iterator:
        def __init__(self, my_list):
            self.curr = my_list.head
        def __next__(self):
            if self.curr:
                res = self.curr
                self.curr = self.curr.next
                return res.val
            raise StopIteration
        def __iter__(self):
            return self    