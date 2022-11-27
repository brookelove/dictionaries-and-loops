'''
1. 2 constants made of last and first names
2. have to ensure that the last names are greater than the first name 
    a. if the first name list is longer return an error and exit system
3. run a for loop that will create a last name as the key and the first name as the value 
4. if the first name is shorter than the last name return the value as None
'''
import sys
LAST_NAMES = ['Doe', 'Deer', 'Black']
FIRST_NAMES = ['Jane', 'Joe']
# zipped_names = ()


def dictionary_of_names():

    if len(LAST_NAMES) <= len(FIRST_NAMES):
        print("Please inpuit more last names than firest names")
        sys.exit()

    if len(LAST_NAMES) >= len(FIRST_NAMES):
        result = len(LAST_NAMES) - len(FIRST_NAMES)
        # print(result)
        for x in range(result):
            FIRST_NAMES.append(None)


    # print(FIRST_NAMES) #returns None in the list of first names
zipped_names = zip(LAST_NAMES, FIRST_NAMES)
# print(dict(zipped_names)) # returns result as a
# return zipped_names


print(f"First Names: {FIRST_NAMES}")
dictionary_of_names()
print(f"Last Names: {LAST_NAMES}")
print(f"Name Dictionary: {dict(zipped_names)}")
# for x in range(len(LAST_NAMES)):
# print(LAST_NAMES[x]) # returns indexed names of the list
# if FIRST_NAMES[x] == IndexError:
#     name_dict[LAST_NAMES[x]] = None
# name_dict[LAST_NAMES[x]] = FIRST_NAMES[x]
