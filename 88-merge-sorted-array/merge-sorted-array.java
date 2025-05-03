class Solution {
    public void moveForward(int[] nums1, int start, int end) {
        for (int i = end; i > start; i--) {
            nums1[i] = nums1[i - 1];
        }
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j = 0;
        int total = m; 

        for (int i = 0; i < total && j < n; i++) {
            if (nums1[i] > nums2[j]) {
                moveForward(nums1, i, total);
                nums1[i] = nums2[j];
                j++;
                total++;
            }
        }

        while (j < n) {
            nums1[total++] = nums2[j++];
        }
    }
}
