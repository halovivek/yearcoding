def decorator(func):
    def to_be_added():
        print(" i got decorated")
        func()
    return to_be_added

#func("this is testing")

@decorator
def normal_function():
    print(" i am testing the decorator, it should print both values")


normal_function()

added_functions = decorator(normal_function)
added_functions()