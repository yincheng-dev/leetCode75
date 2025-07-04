public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int [] output = new int [n];

        output[0] =1;
        for (int i=1;i<n;i++)
        {
            output [i] = nums [i-1] * output [i-1];
        }

        int suffix =1;
        for (int i=n-1 ;i >=0; i--)
        {

            output[i] = output [i]*suffix; 
            suffix = suffix * nums [i]; 
        }
        return output; 
    }
}