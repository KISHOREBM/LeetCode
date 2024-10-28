class Solution {
    public long minimumSteps(String s) {
        long count = 0;
        long white=0;

        for(char c: s.toCharArray())
        {
            if(c=='0')
            count+=white;
            else 
            white+=1;
            // else
            // white=0;
        }
        return count;
    }
}