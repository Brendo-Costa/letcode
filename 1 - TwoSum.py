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

nums = []

while True:
    num = input('Informe o número do vetor: ')
    condicao = input('Deseja adicionar mais elementos? [s/n]')
    nums.append(num)
    if condicao == 'n':
        print(nums)
        break
    
def TwoSuns(nums, target):
    for indice1, num1 in enumerate(nums):
        for indice2, num2 in enumerate(nums):
            if indice1 != indice2:
                soma = num1+num2
                if soma == target:
                        
                    print(num1, num2)
                    print(indice1, indice2)
                    #if soma == target:
                    #    print(indice1, indice2)
                    
                
                
target = input('Infome o valor do target: ')
TwoSuns(nums, target)