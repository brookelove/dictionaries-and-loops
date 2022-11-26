'''
1.at least 15 characters in a string 
    a. if statement that says 15 < len(string) then sys.exit()
2. split sentence
3. have a for loop to run over list 
4. print currentl letter and a list and then add one to tally mark 
    a. append the element if not in list 
    b. then add a tally mark to the list
'''
import sys
analyze_string = "Was it a rat I saw?"

if len(analyze_string) <= 15:
    print(
        f"Please present a sentence with 15 characters or more: {len(analyze_string)}")
    sys.exit()


print(f"The string being analtzed is: {analyze_string}")
print(f"1. Dictionary of letter counts: ")
print(f"2. Most frequent letter(s) _ appears _ times")
