""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
""" 
def two_sum(nums, target):
    # Dicionário para armazenar os números visitados e seus índices
    num_dict = {}
    
    # Itera sobre a lista de números
    for i, num in enumerate(nums):
        complement = target - num
        
        # Verifica se o complemento já está no dicionário
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Armazena o número e seu índice no dicionário
        num_dict[num] = i

# Exemplo de uso
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Retorna [0, 1]                                                                                                                                                                                                                                                                  
<<<<<<< HEAD
            
=======
 """
 
 
 
def TwoSum(nums, target):
    
    nums_dict = {} #Chave:Valor -> Inteiro:Index
    
    for index, num in enumerate(nums):
        complement = target - num
        nums_dict[num] = index
        if complement in nums_dict:
            print(nums_dict[complement], index)
        
    print(nums_dict)
    
    
lista = [1, 2, 3, 4, 5]
TwoSum(lista, 5)
>>>>>>> 135673c614be37a99642b7abb4fdaee90d9c1194
