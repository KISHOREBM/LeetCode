class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        
        max_right = [0] * n  # Stores max value to the right of each index
        max_right[-1] = nums[-1]
        
        # Compute suffix max in one pass
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], nums[i])
        
        max_left = nums[0]  # Keeps track of max value on the left
        max_triplet = 0
        
        # Iterate through the middle element
        for j in range(1, n-1):
            diff = max_left - nums[j]
            if diff > 0:
                max_triplet = max(max_triplet, diff * max_right[j+1])
            max_left = max(max_left, nums[j])  # Update left max
        
        return max_triplet
