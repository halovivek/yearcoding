import os
import pandas as pd
import csv
path = "//home//halovivek//Downloads//education//Jimi Kwik - Super Brain//"
list =[]
for (root,dirs, file) in os.walk(path):
    for f in file:
        file.sort()
        print(f)

fields = ['directory','filename']
filename = "testing.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(root)
    csvwriter.writerows(dirs)

