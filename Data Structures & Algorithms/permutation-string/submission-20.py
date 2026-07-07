class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): 
            return False
        
        s1_map = {}
        s2_map = {}
        for i in range(len(s1)):
            s1_map[s1[i]] = 1 + s1_map.get(s1[i], 0)
            s2_map[s2[i]] = 1 + s2_map.get(s2[i], 0)

        left = 0
        for right in range(len(s2)):
            s2_map[s2[right]] = 1 + s2_map.get(s2[right], 0)
            
            char_to_remove = s2[left]
            s2_map[char_to_remove] -= 1

            if s2_map[char_to_remove] == 0:
                del s2_map[char_to_remove]
            
            left += 1

            if s1_map == s2_map:
                return True

        return False