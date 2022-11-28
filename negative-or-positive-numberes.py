'''
1. create constant dictionary 
    a. keys are ' numbers 1-9, - and .'
    b. values are the numbers as words negative for (-) amd point for (.)
2. while loop 
    a. prompt use for enter a number 
    b. enter a try exempt loop 
    c. if they enter the correct number without commas and characters then break out of the loop 
3. for loop to run through dictionary 
    a. if key in dictionary 
        i. get value
        ii. append to list 
        iii. join list 
'''
import string


class IncludedComma(Exception):
    pass


class IncludedLetters(Exception):
    pass


NUMBERS_DICT = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '-': 'negative', '.': 'point'}
user_input = ''
number_lst = []


def get_user_input():
    user_input = input("Enter a number: ")
    user_input_lst = list(user_input)
    for x in range(0, len(user_input_lst)):
        if user_input_lst[x] in string.ascii_lowercase:
            print(f'"{user_input}" is not a valid number. Please try again')
            raise IncludedLetters
    if ',' in user_input:
        raise IncludedComma
    # if user_input_lst == NUMBERS_DICT.keys():
    #     print()
    for key in user_input_lst:
        value = NUMBERS_DICT[key]
        # print(value) # returns the corresponing value from teh input of key
        number_lst.append(value)
    for i in range(len(number_lst)):
        number_lst[i] = number_lst[i].capitalize()
    joined_numbers_as_text = ' '.join(number_lst)

    print(f"As Text: {joined_numbers_as_text}")

    # for x in user_input_lst:
    #     value = list(NUMBERS_DICT.items)[x]
    #     print(value)
    # print(value)
    # for x in range(0, len(user_input_lst)):
    # print(user_input_lst[x])  # list of all information
    # print(NUMBERS_DICT.keys())  # prints list of keys
    # if user_input_lst[x] in NUMBERS_DICT.keys():
    #     value = list(NUMBERS_DICT.values())[x]
    #     print(value)
    # for value in NUMBERS_DICT.values():
    #     print(x)
    # for y in range(0, len(user_input_lst)):
    # print(user_input_lst[y])
    # value = list(NUMBERS_DICT.values())[x]
    # print(value)
    # for key in NUMBERS_DICT.items():
    #     print(user_input_lst[key])
    # user_int = int(user_input)
    # print(user_input_lst)
    # x = 0
    # for x in range(0, len(user_input_lst)):
    #     # print(user_input_lst[x])
    #     if user_input_lst[x] in NUMBERS_DICT.keys():
    #         # print(user_input_lst[x])
    #         for y in user_input_lst:
    #             number_value = NUMBERS_DICT.get('x')
    #             print(number_value)
    #             # number_lst.append(user_input_lst[x])
    #             x += 1
    # for key in range(len(user_input_lst)):
    #     print(user_input_lst[key])
    #     for value in NUMBERS_DICT:
    #         number_value = NUMBERS_DICT.get(key, value)
    #     key += 1
    #     print(value)

    # for key in NUMBERS_DICT.items():
    #     if key in user_input_lst:
    #         for value in range(0, len(user_input_lst)):
    #             print(value)
    # print(value)
    #     number_value = NUMBERS_DICT.get(key)
    #     print(number_value)
    # number_value = NUMBERS_DICT.get(key)
    # print(number_value)
    # print(number_lst)


def main():
    done = False
    while not done:
        try:
            get_user_input()
            done = True
        except IncludedComma:
            print("Please try again without entering a comma")
        except IncludedLetters:
            pass


main()
