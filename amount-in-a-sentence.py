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
# print(sentence_dict)
print(f"The string being analtzed is: {analyze_string}")
print(f"1. Dictionary of letter counts: ")
print(f"2. Most frequent letter(s) _ appears _ times")
