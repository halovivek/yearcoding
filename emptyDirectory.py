import os
for root, dirs, files in os.walk('D:\\recheck'):
    for file in files:
        src_file = os.path.join(root, file)
        if os.path.getsize(src_file) == 0:
            os.remove(src_file)

dir_list = []
for root, dirs, files in os.walk('D:\\recheck'):
    dir_list.append(root)
for root in dir_list[::-1]:
    if not os.listdir(root):
        os.rmdir(root)