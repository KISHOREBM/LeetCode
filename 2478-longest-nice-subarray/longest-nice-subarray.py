class Solution(object):
    def longestNiceSubarray(self, nums):
        used = 0  # Tracks OR of the current subarray
        left = 0  # Left pointer of the window
        max_length = 0  # Stores the longest nice subarray length

        for right in range(len(nums)):
            # If adding nums[right] causes conflict, shrink window from the left
            while (used & nums[right]) != 0:
                used ^= nums[left]  # Remove nums[left] from OR tracker
                left += 1  # Move left pointer
            
            used |= nums[right]  # Add nums[right] to OR tracker
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
