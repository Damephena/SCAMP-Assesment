'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
Should return an array of all the anagrams or an empty array if there are none.

Test Cases: 
A) 'abba', ['aabb', 'abcd', 'bbaa', 'dada']
B) 'racer', ['crazer', 'carer', 'racar', 'caers', 'racer']
C) 'laser', ['lazing', 'lazy',  'lacer']

Excepted output for all test cases:
A) ['aabb', 'bbaa']
B) ['carer', 'racer']
C) [] //empty array

'''

def findie(sample_word, word_list):
    result = [word for word in word_list if sorted(sample_word) == sorted(word)]
    return result

word, word_list = 'abba', ['aabb', 'abcd', 'bbaa', 'dada']

print(findie(word, word_list))
