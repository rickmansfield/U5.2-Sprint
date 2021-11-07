"""

"""
def checkBlanagrams(word1, word2):
    count = 0 
    w1 = set(word1) #Tom Used this yesterday in office hours
    w2 = set(word2)
    diff = w1.difference(w2) or w2.difference(w1)
    if (len(diff)) == 1: 
        return True
    if (len(diff)) == 0: 
        for w in w1: 
            count += abs(word1.count(w) - word2.count)
    if count == 2:
        return True
    return False
print(checkBlanagrams("tanagram", "anagram"))
print(checkBlanagrams("tanagram", "pangram"))
print(checkBlanagrams("aba", "bab"))
print(checkBlanagrams("silent", "listen"))