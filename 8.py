from functools import partial

def deprecated(f = None, *,since = '', will_be_removed = 'future version'):
    #Если функция была вызвана с параметрами
    #Вернуть её частично, примененную
    if f is None:
        if since != '':
            since = ' since version ' + since
        if will_be_removed != 'future version':
            will_be_removed = 'version ' + will_be_removed
        return partial(deprecated, since = since, 
                    will_be_removed = will_be_removed)
    def inner(*args, **kwargs):
        out = f"Warning: function {f.__name__} is deprecated{since}. It will be removed in {will_be_removed}"
        print(out)
        return f(*args, **kwargs)
    return inner
@deprecated(will_be_removed = '5.0.1')
def foo():
   print('Why we still here just to suffer')

foo()


