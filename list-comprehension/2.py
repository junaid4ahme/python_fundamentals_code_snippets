def func1(text):
    return text.upper()


def func2(text):
    return text.lower()

def greet(x):
    greeting = x("This is Text")
    print(greeting)



greet(func1)
