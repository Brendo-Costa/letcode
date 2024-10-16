""" 
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

def addTwoNumbers(list1, list2):
    
    invertido1 = list(reversed(list1))
    invertido2 = list(reversed(list2))
    
    print(invertido1, invertido2)
    
    num1 = ''
    num2 = ''
    for num in invertido1:
        num1 = num1 + str(num)
    for num in invertido2:
        num2 = num2 + str(num)

    print(num1, num2)
    sum = int(num1) + int(num2)
    print(sum)
    
list1 = [2,4,3]
list2 = [5,6,4]
addTwoNumbers(list1, list2)