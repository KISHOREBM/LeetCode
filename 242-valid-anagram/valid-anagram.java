class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        return false;
        // Map<Character,Integer> strs = new HashMap();
        // Map<Character,Integer> strt = new HashMap();
        // for(int i=0; i<s.length(); i++)
        // {
        //     if(strs.get(s.charAt(i))==null)
        //     strs.put(s.charAt(i),1);
        //     else
        //     strs.put(s.charAt(i),strs.get(s.charAt(i))+1);
        //     if(strt.get(t.charAt(i))==null)
        //     strt.put(t.charAt(i),1);
        //     else
        //     strt.put(t.charAt(i),strt.get(t.charAt(i))+1);
        // }
        // if(strs.equals(strt))
        // return true;
        // else
        // return false;
        // for(int i=0;i<s.length();i++)
        // {
        //     strs.put(s.charAt(i),strs.getOrDefault(s.charAt(i),0)+1);
        //     strs.put(t.charAt(i),strs.getOrDefault(t.charAt(i),0)-1);
        // }
        // for(int c : strs.values())
        // {
        //     if(c !=0)
        //     return false;
        // }
        // return true;
        int record[] = new int[26];
        for(int i=0;i<s.length();i++)
        {
            record[s.charAt(i)-'a']++;
            record[t.charAt(i)-'a']--;
        }
        // for(char c: t.toCharArray())
        // {
        //     record[c-'a']--;
        // }
        for(int i: record)
        {
            if(i!=0)
            return false;
        }
        return true;
    }
}