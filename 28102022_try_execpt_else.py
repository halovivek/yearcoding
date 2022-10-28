try:
    print("Input the first number")
    x = int(input())
    print("Input the second number")
    y = int(input())
    if y == 0:
        raise Exception("you cannot divide by zero, program quitting")
    print(x/y)
except Exception as e:
    print(e)
    print("Error occurred")

else:
    print("Code ran successfully")

finally:
    print("Whole block is executed")