class Solution(object):
    def compress(self, s):
        count, slow, fast = 0, 0, 0
        while fast < len(s):
            # write character
            s[slow] = s[fast]
            while s[fast] == s[slow]:
                count += 1
                fast += 1
                if fast == len(s):
                    break

            slow += 1
            # write count if count > 1
            if count > 1:
                count = str(count)
                for c in count:
                    s[slow] = c
                    slow += 1
            count = 0 # reset count
        return slow