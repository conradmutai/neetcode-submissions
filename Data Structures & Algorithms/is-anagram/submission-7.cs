public class Solution {
    public bool IsAnagram(string s, string t) {
            if(s.Length != t.Length) {
                return False
            }

            Dictionary<char, int> s_map = Dictionary<char, int>();
            Dictionary<char, int> t_map = Dictionary<char, int>();

            for(int i = 0; i < s.Length; i++) {
                s_map[s[i]] = s_map.GetValueOrDefault(s[i], 0) + 1
                t_map[t[i]] = s_map.GetValueOrDefault(t[i], 0) + 1
            }

            return s_map.Count == t_map.Count && !s_map.Except(t_map).Any()
    }
}
