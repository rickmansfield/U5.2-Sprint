Established min at zero and max as the given numbers length less one. 
While - Using a while loop as long as the min was less than the max ... 
*  -Used a variable to hold basically a "guess" using sum // floor division 2 
 * - if each guess was == target then I just returned that guess. 
* - otherwise, elif the half was left-handed (I could have done right-handed too) a second conditional could be used   to then check between the min and the new end (left to center) and if max was == guess then it is reset to that value otherwise min is reset to the guess +1. 
* -else if to check the other side if right then +1 other wise like above max gets reset to the guess. 
* then if nothing corresponds just return -1 per specs