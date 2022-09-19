"""
Packing list and removing program - Got the program from Twitter and
i am using here for practicing.
"""
"""
Getting the input from the user and storing and deleting the package
"""
packing_list =[]

while True:
    action = input("what would you like to do?     \n"
                          "1. Exit Program  \n"
                            "2. Add item to the list  \n"
                            "3. Remove item from the list \n"
                            ".......:")
    if int(action) ==1:
        print("Thank you ")
        break
    elif int(action) == 2:
        item = input("which item i need to add ?")
        packing_list.append(item)
        print(packing_list)
    elif input(action) == 3:
        index = input("which item i need to remove?")
        index = int(index)
        packing_list.remove(packing_list[index])
        print(packing_list)

