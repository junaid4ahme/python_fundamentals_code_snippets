# nested functions

def function1(name):
    print("hello {}".format(name))

def function2(name):
    print("{} How you doing ?".format(name))

def function3(name):
    print("Dear Learner")


function3(function1("jack"))
 