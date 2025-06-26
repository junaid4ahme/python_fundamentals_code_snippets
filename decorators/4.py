def divider(function):
    def wrapper():
        print("wrapper started")
        function()
        print("wrapper executed")
    return wrapper


@divider
def corrector():
    print("this is the corrector")


corrector()




