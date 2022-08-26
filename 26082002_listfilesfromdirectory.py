import os
import pandas as pd
path = "//home//halovivek//Downloads//education//Jimi Kwik - Super Brain//"
list = []
for (root,dirs, file) in os.walk(path):
    for f in file:
        print(f)

my_data = pd.DataFrame(file)
my_data.to_excel("outputfile.xlsx", index = False, header= False)

