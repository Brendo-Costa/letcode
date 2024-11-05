"""
    Duplicate Integer
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

def duplicateInteger(nums):
    integer_dict = {}
    
    for index, num in enumerate(nums):
        integer_dict[index] = num
        if num in integer_dict:
            return True
    return False


num_list = [1, 2, 3, 4, 5, 5]
result = duplicateInteger(num_list)
print(result)

