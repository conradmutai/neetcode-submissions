class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> charMap1 = new HashMap<>();
        HashMap<String, Integer> charMap2 = new HashMap<>();

        for (char c : s) {
            charMap1.put(c);
        }
        for (char c : t) {
            charMap2.put(c);
        }

        if(charMap1.equals(charMap2)) {
            return true;
        } else {
            return false;
        }
    }
}
