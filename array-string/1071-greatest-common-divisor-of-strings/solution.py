import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        minLength = ""
        maxLength = ""
        
        if str1 + str2 == str2 + str1:
            print("GCD exists")
            if len(str1) > len(str2):
                maxLength = len(str1)
                minLength = len(str2)
            else:
                maxLength = len(str2)
                minLength = len(str1)

            return str1[:math.gcd(maxLength, minLength)]
        else:
            return ""