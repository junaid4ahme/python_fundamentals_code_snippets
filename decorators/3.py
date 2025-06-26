def function1(function):                    # main function
    def wrapper():                          # wrapper function
        print("hello")                      # command
        function()                          # executing expected function
    return wrapper                          # return wrapper function


@function1                                  # syntax
def function2():                            # define expected function
    print("junaid")

function2()                                 # execute expected function
