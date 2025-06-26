# Decorators they are used to call a function within a function and 
# they are used to modify the functionality of a function.

def decorator_function(inner_function):
    def starter():
        print("Starting a function")
        inner_function()
        print("Done")
    return starter


@decorator_function
def myfunc():
    print("This is the function")


myfunc()
