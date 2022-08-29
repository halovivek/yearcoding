import os
import glob
files_list = []
for root, directories, files in os.walk("//home//halovivek//Downloads//Telegram Desktop//"):
   for name in files:
      files_list.append(os.path.join(root, name))
      file_list = glob.glob("//home//halovivek//Downloads//Telegram Desktop//*.xlsx")
print(files_list)
