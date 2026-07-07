class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> charMap1 = new HashMap<>();
        HashMap<String, Integer> charMap2 = new HashMap<>();

        for (string str : s) {
            charMap1.put(str);
        }
        for (string str : t) {
            charMap2.put(str);
        }

        if(charMap1.equals(charMap2)) {
            return true;
        } else {
            return false;
        }
    }
}
