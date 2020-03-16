def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        # merge-sort elements one-by-one
        for string in strs:
            sortedStr = "".join(sorted(string))                  # SORTED() = FASTER THAN MERGE-SORT
            # check if sorted-version is in a HT
            if sortedStr in dict:
                dict[sortedStr].append(string)
            else:
                dict[sortedStr] = [string]
        
        return [[string for string in dict[group]] for group in dict]