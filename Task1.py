def checkBlanagrams(word1, word2):
    if word1 == "" or word2 == "":
        return False
    work_string = ''
    diff = 0
    sort1 = sorted(word1)  # O(n) space O(nlogn) time
    sort2 = sorted(word2)  # O(n) space O(nlogn) time
    for i in range(len(word1)-1):  # O(n)
        # check for substitutions
        if sort1[i] != sort2[i]:
            diff += 1
        work_string += word1[i] # O(n) space
    # print(work_string)
    # print(word1)
    count = 0
    # check if there was more than 1 substitution made
    for i in range(len(work_string)):  # O(n)
        if work_string[i] not in word2:
            count += 1
    # print('count:', count)
    # if more than 1 substitution return False
    if count > 1:
        return False
    # if no substitutions return false
    if diff == 0:
        return False
    if sorted(work_string) == sorted(word1):
        return True
    return False

print(checkBlanagrams("tanagram", "anagram"))
print(checkBlanagrams("tanagram", "pangram"))
print(checkBlanagrams("aba", "bab"))
print(checkBlanagrams("silent", "listen"))