class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for letter in s.lower():
            if letter.isalnum():
                newStr += letter
        
        if newStr == newStr[::-1]:
            return True
        else:
            return False