def spam(divideBy):
    try:
        return 42 / divideBy
        #print(spam())
    except ZeroDivisionError:
        print("Error: Invalid division")

print(spam(2))
print(spam(1))
print(spam(0))
print(spam(33))

