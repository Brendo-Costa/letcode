""" 
    Is Anagram

    Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""


""" def unravelWords(word:str):
    word_dict = {}
    
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    return word_dict

def anagramValidator(s:str, t:str) -> bool:
    unravel_s = unravelWords(s)
    unravel_t = unravelWords(t)

    if unravel_s == unravel_t:
        print(unravel_s, unravel_t)
        return True
    else:
        print(unravel_s, unravel_t)
        return False
    

#s = "racecar"
#t = "carrace"

s = "jar"
t = "jam"
result = anagramValidator(s, t)
print(result) """


def SepareteLetters(word):
    dict_word = {}
    for letter in word:
        if letter in dict_word:
            dict_word[letter] += 1
        else:
            dict_word[letter] = 1 
    print(dict_word)
    return dict_word            

def ValidAnagram(word1, word2):
    separete_word1 = SepareteLetters(word1)
    separete_word2 = SepareteLetters(word2)
    
    if separete_word1 == separete_word2:
        return True
    else:
        return False
    

s = "mja"
t = "jam"
result = ValidAnagram(s, t)
print(result)