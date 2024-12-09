"""
Dado um array de inteiros nums, encontre os dois números cuja multiplicação seja máxima. 
Retorne a multiplicação máxima.

Exemplo:

Input: nums = [1, 5, 4, 5]
Output: 20
Explanation: O máximo é 5 * 4.
"""

def product_two_elements(elements):
    nums_dict = {}
    primeiro_maior = 0
    for num in elements:
        if num > primeiro_maior:
            primeiro_maior = num
    print(primeiro_maior)
    elements.remove(primeiro_maior)
    
    segundo_maior = 0
    for num in elements:
        if num > segundo_maior:
            segundo_maior = num
    elements.remove(segundo_maior)    
    mult = primeiro_maior*segundo_maior
    
    print(mult)

nums = [1, 5, 4, 25]
product_two_elements(nums)    