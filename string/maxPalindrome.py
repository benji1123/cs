class Solution(object):
    def longestPalindrome(self, s):
        charCount = [0]*128 # use array instead of HT => less mem & fast
        for c in s:
            charCount[ord(c)] += 1
        
        # key is, we JUST ret the theoretical max-len, not the PALINDROME
        result = 0
        middleFlag = False
        for c in charCount:
            
            # even-count chars are entirely used
            # odd-count chars have their even component used (i.e. we will neccessarily use 8 of the 9 "a's")
            result += (c//2)*2 
            
            # the palindrome can use a central char (i.e. rac 'e' car)
            if c % 2 == 1:
                middleFlag = True
        
        # use central char if end-result is EVEN
        if result%2 == 0 and middleFlag:
            return result + 1
        return result