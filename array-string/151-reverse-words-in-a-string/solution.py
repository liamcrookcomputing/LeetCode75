class Solution:
    def reverseWords(self, s: str) -> str:
        left = len(s) - 1
        right = len(s) - 1
        reverseWords = []

        while left >= 0:
            if (' ' not in s[right] and ' ' not in s[left]) and (left == 0 or ' ' in s[left-1]) and (right == len(s)-1 or ' ' in s[right+1]):
                reverseWords.append(s[left:right+1])
                left -= 1
            left -= 1
            if ' ' in s[left+1]:
                right = left

        print(reverseWords)
        return " ".join(reverseWords)