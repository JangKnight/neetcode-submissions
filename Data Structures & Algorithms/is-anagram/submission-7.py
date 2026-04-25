class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_map = {}
        t_freq_map = {}
        for letter in s:
            s_freq_map[letter] = s_freq_map.get(letter, 0) + 1
        
        for letter in t:
            t_freq_map[letter] = t_freq_map.get(letter, 0) + 1
        
        for letter in s_freq_map:
            if s_freq_map.get(letter, 0) != t_freq_map.get(letter, 0):
                return False



        
        return True