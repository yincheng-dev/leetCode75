public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        //create hashset
        HashSet<int>seen = new HashSet<int>();
        //loop through the list and if hashset contains the num , we return true
        foreach (int num in nums){
            if(seen.Contains(num)){
                return true;
            }
            //each time we also add the num into the seen list
            seen.Add(num);
        }
        //after the loop , if nothing found , we return false
        return false;


    }
}