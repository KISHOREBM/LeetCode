class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double res[] = new double[nums1.length+nums2.length];
        int i=0,j=0,k=0;
        while(i<nums1.length && j<nums2.length)
        {
            if(nums1[i]>nums2[j])
            {
                res[k++]=nums2[j++];
            }
            else{
                res[k++]=nums1[i++];
            }
        }
        while(i<nums1.length)
        res[k++]=nums1[i++];
        while(j<nums2.length)
        res[k++]=nums2[j++];
        if(k%2==0)
        return ((double)res[k/2-1]+(double)res[k/2])/2;
        else
        return res[k/2];
    }
}