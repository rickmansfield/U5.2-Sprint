First I had to research Blanagram. The hardes part was wrapping my head around what a blanagram is so that I get the U in U.P.E.R... really sucked. 

- set up edge case where either submission is "". 
- at some point rule out words of different lengths are not blanagrams. 
- initiate empty string to capture new words StringHorse
- need a counter for differences
- need variables for sorting word1 and word2
- loop over the word1 and establish conditionals
- for each letter in the range of first word1 (checking for substitutions) if sorted word1 not same as sorted word2 add to counter otherwise StringHorse gets += word1 . 
- I'll have to reset the counter I think here
- then I'll have to check for other substitutions using 
- I'll need another loop for each char in StringHorse
checking StringHorse against word2 using a conditional i.e. if char StringHorse[i] 
- 
scratch all that... I think I can use Hash Tables and a Counter... Oh thank god... LOL I found in my practice problems the use of Counter and .values() and figured it out. It was exhausting. LOL
