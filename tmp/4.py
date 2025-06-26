# DECORATOR FUNCTION WITH WRAPPER
def smart_div(function):  # here function is variable
    def wrapper(a, b):  # here the arguments should be same as parent function.
        if a < b:  # function commands
            a, b = b, a
        return function(a, b)  # return the function with same arguments as parent function
    return wrapper  # return the wrapper


@smart_div  # decorator syntax
def divider(a, b):  # define the parent function
    return a / b


res = divider(5, 10)  # run the parent functions

print(res)

# CONCLUSION
# here we have run the function, and we kept the parent function intact.
