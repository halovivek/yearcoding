import os
import glob
import pandas as pd
file_list = glob.glob("//home//halovivek//Downloads//Telegram Desktop//*.xlsx")
files = []
for filename in file_list:
    df = pd.read_excel(filename)
    files.append(df)
frame = pd.concat(files, axis=0, ignore_index=True)
print(frame)