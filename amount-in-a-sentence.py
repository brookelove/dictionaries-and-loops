'''
1.at least 15 characters in a string 
    a. if statement that says 15 < len(string) then sys.exit()
2. split sentence
3. have a for loop to run over list 
4. print currentl letter and a list and then add one to tally mark 
    a. append the element if not in list 
    b. then add a tally mark to the list
'''
import string
import sys

analyze_string = "Was it a rat I saw in there?"
counter = 0
sentence_dict = {}
frequent_letters = {}
max_value = []


def split(sentence):
    if len(sentence) <= 15:
        print(
            f"Please present a sentence with 15 characters or more: {len(sentence)}")
        sys.exit()
    analyze_lst = list(sentence.lower())
    return analyze_lst
# print(analyze_lst)
# print(string.ascii_lowercase)


for i in split(analyze_string):
    if i in sentence_dict:
        # print(i)  # prints each element found that is in a list
        # print(i)
       # print(sentence_dict.get(i))  # returns the counter amount
       # print(type(sentence_dict.get(i))) # returns int
        counter = sentence_dict.get(i) + 1
        counter += 1
    elif i in string.ascii_letters:
        counter += 1
        # print(counter)
        sentence_dict[i] = counter
        counter = 0
#  print(sentence_dict)
# max_value = max(sentence_dict, key=sentence_dict.get)
# max_value = [key for key, value in sentence_dict.items() if value ==
#              max(sentence_dict.values())]

for key, value in sentence_dict.items():
    if value == max(sentence_dict.values()):
        # print("max value")
        # print("key", key)
        # print("value", value)
        frequent_letters[key] = value
# print(max_value)
# print(str(frequent_letters.keys()))  # returns list of keys
joined_frequent_letters = ", ".join(frequent_letters.keys())
# print(", ".join(frequent_letters.keys()))  # r, n, h
print(f"The string being analtzed is: {analyze_string}")
print(f"1. Dictionary of letter counts: {sentence_dict}")

# print(len(sentence_dict))
if len(sentence_dict) == 1:
    print(
        f"2. Most frequent letter {joined_frequent_letters} appears {list(frequent_letters.values())[0]} times")
else:
    print(
        f"2. Most frequent letter(s) {joined_frequent_letters} appears {list(frequent_letters.values())[0]} times")
