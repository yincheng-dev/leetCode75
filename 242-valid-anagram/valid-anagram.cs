public class Solution {
    public bool IsAnagram(string s, string t) {
        //First check if the length of the s and t string are the same, 
        //if not just return false
        if (s.Length != t.Length) return false;
        //convert s into a character array 
        char[ ] sSort = s.ToCharArray();
        char[ ] tSort = t.ToCharArray();
        //sort the arraz alphabetically
        Array.Sort(sSort);
        Array.Sort(tSort);
        //Compare the two sorted array Element by Element
        return sSort.SequenceEqual ( tSort );
    }
}