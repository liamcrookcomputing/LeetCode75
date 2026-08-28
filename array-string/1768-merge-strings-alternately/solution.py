class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedString = ''
        word1Length = len(word1)
        word2Length = len(word2)

        if word1Length > word2Length:
            maxLength = word1Length
        else:
            maxLength = word2Length

        for x in range(maxLength):
            if x < word1Length:
                mergedString += word1[x]
            if x < word2Length:
                mergedString += word2[x]

        return mergedString