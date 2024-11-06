class Solution {
    public String bitform(int a)
    {
        String ret="";
        while(a>0)
        {
            int rem=a%2;
            ret+=rem;
            a=a/2;
        }
        return  ret;
    }
    public boolean canswap(int a, int b)
    {
        String bita=bitform(a),bitb=bitform(b);
        int counta=0,countb=0,i=0,j=0;
        while(i<bita.length() && j<bitb.length())
        {
            if(bita.charAt(i)=='1')
            counta+=1;
            if(bitb.charAt(j)=='1')
            countb+=1;
            i++;j++;
        }
        while(i<bita.length()){
        if(bita.charAt(i)=='1')
        {
            counta++;
        }
        i++;}
        while(j<bitb.length()){
        if(bitb.charAt(j)=='1')
        {
            countb++;
        }
        j++;}
        if(counta==countb)
        return true;
        return false;
    }   
    public boolean canSortArray(int[] nums) {
        for(int i=0;i<nums.length;i++)
        {
            for(int j=0;j<nums.length-i-1;j++)
            {
                if(nums[j]>nums[j+1])
                {
                    if(canswap(nums[j],nums[j+1]))
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