
#decorators write a function and make it as decorator.

def hasha(func):
    def inner(*args,**kwargs):
        print("#" * 50)
        func(*args,**kwargs)
        print("#" * 50)
    return inner

def dash(func):
    def inner(*args, **kwargs):
        print("-" * 50)
        func(*args,**kwargs)
        print("_" * 50)
    return inner

@hasha
@dash
def show(greetings):
    print(greetings)


show("OVM")