'''
1. create a constant list of integers
2. using a range function from 55 to 5 with a stop of 10 append each item to a list
3. take each elment and sum it next to its neighbor, so that 55 + 45 = 100, then 55+ 45+ 35 = 135, then so on and so forth
    a. two for loops?
'''
# STEP 01: constant list of variables
LST_OF_INT = []
RESULT_LST = []
added_val = 0
# STEP 02: create a for loop with a range of functions that will go through integers with a number that is then appended to teh constant list
for x in range(5, 65, 10):
    LST_OF_INT.append(x)
MAX_VALUE = len(LST_OF_INT)

reverse_lst = LST_OF_INT[::-1]  # returns the list in reverse
print("Input List: ", reverse_lst)

# for i in range(0, len(LST_OF_INT)):
#     added_val = added_val + LST_OF_INT[i]
# RESULT_LST.append(added_val)
# print(RESULT_LST)


# for i in range(0, len(LST_OF_INT)):
#     LST_OF_INT.pop()
#     print(LST_OF_INT)
#     for j in range(i + 1, len(LST_OF_INT)):
#         added_val = added_val + LST_OF_INT[j]
#         RESULT_LST.append(added_val)
#         print(added_val)
# print(RESULT_LST)


for i in range(-1, len(reverse_lst)):
    if len(reverse_lst) == 1:
        break
    # print(reverse_lst)
    # print(sum(reverse_lst))
    RESULT_LST.append(sum(reverse_lst))
    reverse_lst.pop()
    # for number in range(i+1, len(LST_OF_INT)):
    #     print(sum(LST_OF_INT))

print("Result List: ", RESULT_LST[::-1])
# print(RESULT_LST)
# added_val = added_val + LST_OF_INT[i]
# print(added_val)
# print(LST_OF_INT)
# LST_OF_INT.pop()
# for j in range(i + 1, len(LST_OF_INT)):
# print(LST_OF_INT[j])


# i = 2
# value = LST_OF_INT[0] + LST_OF_INT[1]
# for i in range(5, 65, 10):
#     print(i)
#     for j in i + 1:
#         print(j)
# added_value = value + LST_OF_INT[i]
# SUM_OF_LIST.append(added_value)
# i += 1
# print(f"when you add {LST_OF_INT[i]} + {LST_OF_INT[i+1]}. You get: ",
# LST_OF_INT[i] + LST_OF_INT[i+1]) # prints two togehter 5 and 15 then 15 and 25 and so forth
# for i in range(0, len(LST_OF_INT)):
#     # print(LST_OF_INT[i])
#     # i += 1
#     added_val = added_val + LST_OF_INT[i]
#     print(added_val)

# for i in range(0, MAX_VALUE + 1):
#     LST_OF_INT.pop()
#     print(LST_OF_INT)
# for j in range(i+1, len(LST_OF_INT)):
#     added_val = added_val + LST_OF_INT[j]
#     print(f"{added_val} and {LST_OF_INT[j]}")
#     print(added_val)
