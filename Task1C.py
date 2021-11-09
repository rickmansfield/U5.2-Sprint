"""
THIS ONE WORKS 
"""

from collections import Counter
# print(help(values()))
# returns a list of all the values available in a given dictionary.
# print(help(Counter))
# |  Dict subclass for counting hashable items.  Sometimes called a bag
#  |  or multiset.  Elements are stored as dictionary keys and their counts
#  |  are stored as dictionary values.

def checkBlanagrams(word1, word2):

    firstWordCount = Counter(word1)
    print("firsWordCount to dict", firstWordCount)
    secondWordCount = Counter(word2)
    print("seconWordCount", secondWordCount)

    result1 = sum((firstWordCount - secondWordCount).values())
    print("Result1: ", result1)
    result2 = sum((secondWordCount-firstWordCount).values())
    print("Result2: ", result2)
    return result1 == 1 or result2 == 1 # "or" works becuase you only need one word to be a blanagram of the other not both. 


print(checkBlanagrams("tanagram", "anagram"))
# print(checkBlanagrams("tanagram", "pangram"))
# print(checkBlanagrams("aba", "bab"))
# print(checkBlanagrams("silent", "listen"))