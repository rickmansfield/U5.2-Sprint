Then only significant time complexity is O(n) for Counter for both firstWordCount and sceondWordCount.  But, there are not many "big" words in any language so that would always be closer to O(1)

result1 and result2 also have minimal Big0 for space complexity as storage is only the length of resulting list of all values available in the dictionary. Technically it's also dependent on word size and therefore one could argue O(n) but realistically there are few large words and the true results would mimic O(1) 

So the entire block boils to minimal Time and Space Complexity of worst case of O(n) but will most likely always resemble O(1) due to minimal word sizes used. 