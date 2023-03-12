def diff(x, y):
    return x - y
def min(first, *args):
    res = first
    for x in args:
        res = x if x < res else res
    return res

def specialize(func, *s_args, **s_kwargs):
    def tmp(*args, **kwargs):
        return func(*args, *s_args, **kwargs,**s_kwargs) 
    return tmp

f = specialize(min,42, 52)

print(f(-1))