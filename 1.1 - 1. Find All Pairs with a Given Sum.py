""" 1. Find All Pairs with a Given Sum

Dado um array de inteiros nums e um inteiro target, encontre todos 
os pares únicos de números no array que somam target. Retorne os 
pares como uma lista de listas.

Input: nums = [2, 7, 11, 15, -2, 7], target = 9
Output: [[2, 7], [-2, 11]]
"""
 
def find_all_pairs_with_a_given_sum(nums, target):
    
    #Chave vai ser o valor do elemento e o valor seu índice
    #chave = num, valor = indice
    nums_dict = {}
    sums_list = []
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_dict:
            complement_list = []
            complement_list.append(num)
            complement_list.append(complement)
            sums_list.append(complement_list)

        #chave é o num, valor é seu índice
        nums_dict[num] = index
        
    print(sums_list)

nums = [2, 7, 11, 15, -2]
target = 9
find_all_pairs_with_a_given_sum(nums, target)