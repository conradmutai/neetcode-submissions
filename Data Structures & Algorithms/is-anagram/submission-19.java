class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> charMap1 = new HashMap<>();
        HashMap<String, Integer> charMap2 = new HashMap<>();

        for (String str : s) {
            charMap1.put(str);
        }
        for (String str : t) {
            charMap2.put(str);
        }

        if(charMap1.equals(charMap2)) {
            return true;
        } else {
            return false;
        }
    }
}
