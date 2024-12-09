"""
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    Example 1:

    Input: nums = [1, 2, 3, 3]

    Output: true 
"""


def ContainsDuplicate(nums):
    nums_dict = {}
    duplicate = False
    
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
     
    for value in nums_dict.values():
        if value > 1:
            duplicate = True
            break
        else:
            duplicate = False
    
    return duplicate    

lista_de_numeros = [1, 2, 2, 3]

result = ContainsDuplicate(lista_de_numeros)
print(result)