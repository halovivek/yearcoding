import glob
import os
import pandas as pd
list_of_mp3s_mp4s = []
for file_or_dir in glob.glob("//home//halovivek//Downloads//education//Jimi Kwik - Super Brain//", recursive = True):
        if os.path.isfile(file_or_dir) and file_or_dir.lower().__contains__(".mp3") or file_or_dir.lower().__contains__(".mp4"):
            list_of_mp3s_mp4s.append(file_or_dir)
my_data = pd.DataFrame(list_of_mp3s_mp4s)
my_data.to_excel("outputfile1.xlsx", index = False, header= False)