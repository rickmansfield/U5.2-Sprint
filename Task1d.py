def checkBlanagrams(word1, word2):
    freq = dict()
    for char in (word1 + word2):
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
            
print(checkBlanagrams("tanagram", "anagram"))
# print(checkBlanagrams("tanagram", "pangram"))
# print(checkBlanagrams("aba", "bab"))
# print(checkBlanagrams("silent", "listen")