import imp
from itertools import accumulate
import operator 
a = [1,2,3,4,5,6,7,8,9,2,4,5]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

