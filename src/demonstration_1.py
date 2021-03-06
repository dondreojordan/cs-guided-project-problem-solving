"""
Given a list of integers and a target value, 
return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, 
and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""


def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(len(nums[i+1:])+1):
            if nums[i] + nums[j] == target:
                return i, j


nums = [3, 8, 12, 17]
target = 15
print(two_sum(nums, target))