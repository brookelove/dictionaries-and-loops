import string
MY_DICT = {'a': 15, 'c': 18, 'b': 20}
my_dict_keys = list(MY_DICT.keys())
my_dict_values = ', '.join(map(str, MY_DICT.values()))
sorted_values = sorted(MY_DICT.items(), key=lambda x: x[1])
print(sorted(MY_DICT.items()))
# print(sorted_keys)
# my_dict_values = ", ".join(str(MY_DICT.values()))
my_dict_lst = []
sorted_values_str = ''
for x in range(0, len(MY_DICT)):
    # my_dict_tuple = ()
    # if x in string.ascii_lowercase():
    # print(list(MY_DICT.keys())[x])  # returns individual key
    # print(list(MY_DICT.values())[x])  # returns matching value from key

    my_dict_tuple = (list(MY_DICT.keys())[x], list(MY_DICT.values())[x])
    my_dict_lst.append(my_dict_tuple)
# print(str(my_dict_lst[0][1]))  # returns a tuple
# print(': '.join(str(my_dict_lst[0])))
# print(my_dict_tuple)  # returns current tuple
# for y in range(0, len(MY_DICT)):
#     for z in range(y + 1, len(MY_DICT)):
#         print(list(MY_DICT.values())[y])
#         print(list(MY_DICT.values())[z])
# print(str(my_dict_lst[0:len(my_dict_lst[0])]))
for y in range(0, len(my_dict_lst)+1):
    # for z in range(y+1, len(my_dict_lst)):
    # print(z)
    # if z == len(my_dict_keys):
    #     break
    if y == len(my_dict_keys):
        break
    if my_dict_lst[x] == my_dict_lst[-1]:
        sorted_values_str = f"{sorted_values_str}{str(my_dict_lst[y][0])}: {str(my_dict_lst[y][1])} "
    else:
        # print(str(my_dict_lst[y][0]))
        # print(str(my_dict_lst[y][1]))
        sorted_values_str = f"{sorted_values_str}{str(my_dict_lst[y][0])}: {str(my_dict_lst[y][1])}, "
    # sorted_num_str = f"{str(my_dict_lst[y][0])}: {str(my_dict_lst[y][1])} "
    y += 1
    #     # z += 1
    #     print(str(my_dict_lst[1][z]))
# z = 0
print(sorted_values_str)
print('')
print(f"Keys: {my_dict_keys}")
print(f"Values: {my_dict_values}")
print(f"Key value pairs: {sorted_values_str}")
print(f"Key value pairs ordered by key: {my_dict_lst}")
print(f"Key value pairs ordered by value: {sorted_values_str}")
