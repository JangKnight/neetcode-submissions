class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = {}
        for letter in s:
            freq_map[letter] = freq_map.get(letter, 0) + 1
        
        for letter in t:
            if letter not in freq_map:
                return False
            freq_map[letter] -= 1
            if freq_map[letter] < 0:
                return False


        
        return True