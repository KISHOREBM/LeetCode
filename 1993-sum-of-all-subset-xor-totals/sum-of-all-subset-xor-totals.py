def sum_of_subsets(nums):
    subset_sums = [] 
    n = len(nums)
    for i in range(1 << n):  
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):  
                subset_sum ^= nums[j]
        subset_sums.append(subset_sum)
    
    return subset_sums
class Solution(object):
    def subsetXORSum(self, nums):
        return sum(sum_of_subsets(nums))
        