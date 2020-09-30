"""
Given a `string`, write a function that finds the first non-repeating character in the `string` and return its index. If it doesn't exist, return -1.

Examples:

string = "lambdaschool"
return 2.

string = "lovelambdaschool"
return 2.

string = "abcabc"
return -1.
"""
def first_unique_char(string):
    
    for idx, val in enumerate(string):
        if string.count(val) == 1:
            return print(f'Located at index {idx}')

    return print(f'Located at index {-1}')

# string = "abcabc"
# string = "dondreojordan"
string = "lambdaschool"
print(first_unique_char(string))