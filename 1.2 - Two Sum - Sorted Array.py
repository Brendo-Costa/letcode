""" 
2. Two Sum - Sorted Array

Dado um array ordenado de inteiros nums e um inteiro target,
encontre os índices dos dois números que somam target. Retorne
os índices em ordem crescente. Resolva o problema com complexidade 
O(n) usando dois ponteiros.

Exemplo:

Input: nums = [1, 2, 3, 4, 4, 9], target = 8
Output: [2, 4]
"""

def two_sum(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        
        complement = target - num
        if complement in nums_dict:
            print(nums_dict[num], index)
        
        nums_dict[num] = index

    print(nums_dict)

elements = [1, 2, 3, 4, 4, 9]
target = 8
two_sum(elements, target)