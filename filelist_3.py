# import glob
# import pandas as pd
# file_list = glob.glob("//home//halovivek//Downloads//Telegram Desktop//*.xlsx")
# files = []
# for filename in file_list:
#     df = pd.read_excel(filename)
#     files.append(df)
# frame = pd.concat(files, axis=0, ignore_index=True)
# print(frame)

# import os
# dir_path = r'//home//halovivek//Downloads//20 Self-Help Books Collection Pack-36//'
# for path in os.scandir(dir_path):
#     if path.is_file():
#         print(path.name)


# import sys, os
#
# try:
#     import pandas as pd
# except:
#     os.system("pip3 install pandas")
#
# root = "//home//halovivek//Downloads//" # it may have many subfolders and files inside
# lst = []
# from fnmatch import fnmatch
#
# pattern = "*.csv"  # I want to get only csv files
# pattern = "*.*"  # Note: Use this pattern to get all types of files and folders
# for path, subdirs, files in os.walk(root):
#     for name in files:
#         if fnmatch(name, pattern):
#             lst.append((os.path.join(path, name)))
# df = pd.DataFrame({"filePaths": lst})
# df.to_csv("filepaths.csv")

import sys, os

root = "//home//halovivek//Downloads//education//"
path = os.path.join(root, "//home//halovivek//Downloads//education//")

for r, d, f in os.walk(path):
    for file in f:
        print(os.path.join(root, file))