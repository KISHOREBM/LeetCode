class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        return false;
        Map<Character,Integer> strs = new HashMap();
        Map<Character,Integer> strt = new HashMap();
        for(int i=0; i<s.length(); i++)
        {
            if(strs.get(s.charAt(i))==null)
            strs.put(s.charAt(i),1);
            else
            strs.put(s.charAt(i),strs.get(s.charAt(i))+1);
            if(strt.get(t.charAt(i))==null)
            strt.put(t.charAt(i),1);
            else
            strt.put(t.charAt(i),strt.get(t.charAt(i))+1);
        }
        if(strs.equals(strt))
        return true;
        else
        return false;
    }
}