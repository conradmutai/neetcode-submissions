class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> charMap1 = new HashMap<>();
        HashMap<Character, Integer> charMap2 = new HashMap<>();

        for (char c : s.toCharArray()) {
            charMap1.put(c, charMap1.get(c) + 1);
        }
        for (char c : t.toCharArray()) {
            charMap2.put(c, charMap2.get(c) + 1);
        }

        if(charMap1.equals(charMap2)) {
            return true;
        } else {
            return false;
        }
    }
}
