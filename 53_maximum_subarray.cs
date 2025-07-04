public class Solution {
    public int MaxSubArray(int[] nums) {
        if (nums.Length == 0) return 0;
    
        int maxGlobal = nums[0];
        int maxCurrent = nums[0];

        for ( int i=1 ;i<nums.Length; i++) {
        maxCurrent =  Math.Max(nums[i],nums[i]+maxCurrent);

        if( maxCurrent>maxGlobal)
        {
            maxGlobal = maxCurrent;
        }

        }
        return maxGlobal;
      
    }
}