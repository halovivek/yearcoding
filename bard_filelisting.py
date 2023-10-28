import os
import csv

# Import the necessary libraries

def get_file_list(directory):

# Define a function to get the list of files in a directory

    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

def write_file_list_to_csv(file_list, filename):

# Define a function to write the list of files to a CSV file

    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["File Name"])
        for file in file_list:
            writer.writerow([file])

# Get the list of files in the current directory

file_list = get_file_list(".")

# Write the list of files to a CSV file

write_file_list_to_csv(file_list, "file_list.csv")
