public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;  // Start from 1 since versions are 1-indexed
        
        while (start < n) {  // Use < instead of <=
            int mid = start + (n - start) / 2;  // Prevent overflow
            if (isBadVersion(mid)) {
                n = mid;  // Move n to mid because mid could be the first bad version
            } else {
                start = mid + 1;  // Move start up because mid is not a bad version
            }
        }
        
        return start;  // At the end, start should be the first bad version
    }
}
