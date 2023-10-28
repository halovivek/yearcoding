import os
import glob
files_list = []
for root, directories, files in os.walk("E:"):
   for name in files:
      files_list.append(os.path.join(root, name))
      file_list = glob.glob("E:\\*.xlsx")
print(files_list)
