class Solution(object):
    def longestPalindrome(self, s):
        # dynamic programming approach
        if s is None or len(s) <=1:
            return s
        
        # PRE-INIT MAP 
        # Matrix -> [i][j] maps to s[i:j] -> s[i][j] = s[i:j] == palindrome
        maxC, maxR = 0, 0 # track longest substring
        
        map = [[False for x in range(len(s))] for row in range(len(s))]
        for i in range(len(s)):
            map[i][i] = True
            if i != len(s)-1 and s[i+1] == s[i]:
                map[i][i+1] = True
                maxC, maxR = i+1, i
        
        # FULLY POPULATE MAP
        for i in range(len(s)-3, -1, -1): # bot-2 rows are pre-initialized!
            # check substrings i : [i+2 ... n]
            for j in range(i+2, len(s)):
                if s[i] == s[j] and map[i+1][j-1]:
                    map[i][j] = True
                    if (j-i) > (maxC-maxR):
                        maxC, maxR = j, i
        
        return s[maxR:maxC+1]