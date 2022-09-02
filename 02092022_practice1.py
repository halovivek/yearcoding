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

