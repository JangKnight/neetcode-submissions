class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for letter in s.lower():
            if letter.isalnum():
                newStr += letter
        
        return newStr == newStr[::-1]