from functools import wraps
def coroutine(func):
    @wraps(func)
    def inner(*args, **kwars):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    
    return inner


