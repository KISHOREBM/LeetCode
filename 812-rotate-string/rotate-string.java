class Solution {
    public boolean rotateString(String s, String goal) {
        if(s.length()!=goal.length())
        return false;
        int i=0,j=0,k=0;
        while(i<s.length())
        {
            if(s.charAt(i)==goal.charAt(0))
            {
                j=i;k=0;
                while(k<s.length() &&s.charAt(j%s.length())==goal.charAt(k))
                {
                    k++;
                    j=(j+1)%s.length();
                }
                if(k==s.length())
                return true;
            }
            i++;
        }
        return false;
    }
}