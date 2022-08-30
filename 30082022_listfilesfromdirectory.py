import os
import pandas as pd
#path of the file you want to enemurate
path = "//home//halovivek//Downloads//"
directory =[]
filename=[]

for (root,dirs, file) in os.walk(path):
    for f in file:
        directory.append(root)
        filename.append(f)
        print(f)

#column name of the sheet
df=pd.DataFrame(list(zip(directory,filename)),columns=['Directory',"filename"])
#change the file of exccl sheet
df.to_csv("all.csv")