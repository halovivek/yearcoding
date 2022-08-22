import math

def add_numbers(*args):
    return sum(args)

def main(number):
    print(f"The square root of the number {number} is {round(math.sqrt(number),4)}")

main(8)