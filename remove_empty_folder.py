import os
import shutil
folder_path = "//home//halovivek//Downloads//education//Books - Investing and Options//Volatility and VIX Collection//"
if len(os.listdir(folder_path)) == 0: # Check is empty..
    shutil.rmtree(folder_path)