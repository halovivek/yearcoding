import os
path = "//home//halovivek//Downloads//education//Jimi Kwik - Super Brain//"
list = []
for (root,dirs, file) in os.walk(path):
    for f in file:
        print(f)

