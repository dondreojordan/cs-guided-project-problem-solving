"""
Given a list of phone numbers, determine if it is consistent in the sense that 
no number in the list is the prefix of another number in the list.

Example

For numbers = ["911", "9876543", "9112345"], the output should be
prefixFreePhones(numbers) = false.
In this case, it isn't possible to call the third person in a list, 
because the system would direct your call to the first number as soon 
as you dialed the first three digits of third phone number. So this list is not consistent.
"""


# def prefixFreePhones(numbers):
    # input: a list phone numbers w/any number of digits
    # Determine what is a prefix? Possibly the first three numbers.
    # Create a list to cross-verify
    # Iterate over each phone number and check is prefix is unique or not. 
    # return: boolean, True means it is consistent and False means there are numbers prefixed as another.
    # return

# def prefixFreePhones(numbers):
#     for prefix in numbers:
#         for cross_ref in numbers:
#             if prefix != cross_ref and prefix in cross_ref:
#                 return False
#     return True


def prefixFreePhones(numbers):
    set_nums = set(numbers)
    for num in numbers:
        for idx in range(1, len(num)):
            if num[:idx] in set_nums:
                return False
    return True

# numbers = ["911", "9876543", "9192345"]
numbers = ["911", "9876543", "9112345"]


if __name__ == '__main__':
    print(prefixFreePhones(numbers))