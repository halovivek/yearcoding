import time


def timetest(input_func):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name - {0}, Agrs - {1}, Kwargs - {2} , Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        ))
        return result

    return timed()

def func(*args, **kwargs):
    time.sleep(0.6)
    print("inside function")
    print(args,kwargs)

func(["Helllo world"], start = 2, end =5)


@timetest
def func(*args, **kwargs):
    time.sleep(0.5)
    print("Inside one more value")
    print(args, kwargs)


def smart_divide(func):
    def inner(a,b):
        print("i am going to divide ",a,"and", b)
        if b == 0:
            print("zero cannot be divided")
            return

        return func(a,b)
    return inner


@smart_divide
def divide(a,b):
    print(a/b)
    #return a/b

divide(3,0)

divide(2345634325324523423423342412424343242434234234234,9707076768768700708)
