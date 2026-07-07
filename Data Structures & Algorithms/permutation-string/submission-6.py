class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}
        left = 0

        for right in range(len(s1)):
            s1_map[right] = 1 + s1_map.get(right, 0)
            right += 1

        for right in range(len(s2)):
            s2_map[right] = 1 + s2_map.get(right, 0)
            
            if s1_map[right] == s2_map[right]:
                return False
            else:
                right += 1
         
        print(s1_map, s2_map)
        return True