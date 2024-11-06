class Solution {
    public String bitform(int a)
    {
        String ret="";
        while(a>0)
        {
            int rem=a%2;
            if(rem!=0)
            ret+=rem;
            a=a/2;
        }
        return  ret;
    } 
    public boolean canSortArray(int[] nums) {
        for(int i=0;i<nums.length;i++)
        {
            for(int j=0;j<nums.length-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    if (bitform(nums[j]).length() == bitform(nums[j + 1]).length())
                    {
                        int temp=nums[j];
                        nums[j]=nums[j+1];
                        nums[j+1]=temp;
                        
                    }
                    else
                    return false;
                }
            }
        }
        return true;
    }
}