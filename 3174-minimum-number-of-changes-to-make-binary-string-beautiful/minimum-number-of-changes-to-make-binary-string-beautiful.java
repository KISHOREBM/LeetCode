class Solution {
    public int minChanges(String s) {
        int changes = 0;

        // Iterate over pairs of characters
        for (int i = 0; i < s.length(); i += 2) {
            // Check if each pair (s[i], s[i+1]) has different characters
            if (s.charAt(i) != s.charAt(i + 1)) {
                changes++;
            }
        }

        return changes;
    }
}
