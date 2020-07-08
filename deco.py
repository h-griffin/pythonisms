from functools import wraps

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print('emphasize')
        # print('before calling original')
        orig_val = f'{func(*args, **kwargs)}!!!'
        # print('after calling orig')
        return orig_val

    return wrapper

def sarcastic_descorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print('sarcastic')
        orig_val = func(*args, **kwargs)
        return f'sure, id love to do "{orig_val}"'
    return wrapper



@sarcastic_descorator
def proclaim(txt):
    print('*** sarcastic proclaim ***')
    return txt

@emphasize
def dinner(txt):
    print('*** emphasized dinner ***')
    return txt

@emphasize
@sarcastic_descorator
def lunch(txt):
    print('*** emphasized sarcastic lunch ***')
    return txt

if __name__ == "__main__":
    print(proclaim('fish'))
    print(dinner('spagetti'))
    print(lunch('sandwiches'))
