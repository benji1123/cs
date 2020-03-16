'''
Fri 10:43 PM, 20 Sept 2019

937. Reorder Data in Log Files (Easy)
    Runtime: 20 ms, faster than 87.46%
    Memory Usage: 11.8 MB, less than 96%
'''
def compareTwoWordLogs(s1, s2):
    
    # log-contents are equal, compare identifiers
    if s1[1] == s2[1]:
        if s1[0] < s2[0]: return -1     # already in ascending-order
        else: return 1
    # compare log-contents
    else:
        if s1[1] < s2[1]: return -1     # already in ascending-order
        return 1   
    
class Solution(object):
    def reorderLogFiles(self, logs):

        # separation of concerns, split word & number logs
        wordLogs, numLogs = [], []
        for log in logs:
            if log[-1].isalpha():
                _temp = log.split(' ')
                wordLogs.append([_temp[0], ' '.join(_temp[1:])])
            else:
                numLogs.append(log)
        
        # sort wordLogs
        wordLogs.sort(cmp = compareTwoWordLogs)
        return ([log[0] + ' ' + log[1] for log in wordLogs]) + numLogs
            
        
