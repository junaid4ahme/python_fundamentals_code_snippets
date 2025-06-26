
def smart_div(function):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        return function(a, b)
    return wrapper


@smart_div
def divider(a, b):
    return a / b

divider(10, 2)



