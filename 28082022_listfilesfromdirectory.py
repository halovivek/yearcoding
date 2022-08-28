import os
import pandas as pd
path = "//home//halovivek//Downloads//education//Jimi Kwik - Super Brain//"
data = []
for file in os.listdir(path):
    data.append(file)
    print(file)

df = pd.DataFrame(data, columns=['Files'])
df.to_excel("mylist.xlsx", index=False)

