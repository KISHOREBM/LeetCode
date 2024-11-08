class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int n = nums.length;
        int[] result = new int[n];
        int max = (1 << maximumBit) - 1;
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        for (int i = 0; i < n; i++) {
            result[i] = xor ^ max;
            xor ^= nums[n - i - 1];
        }
        
        return result;
    }
}
