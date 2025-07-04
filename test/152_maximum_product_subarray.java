class Solution {
    public int maxProduct(int[] nums) {
        int max_so_far = nums [0];
        int min_so_far = nums [0];
        int result = nums [0];

        for (int i = 1; i<nums.length; i++)
        {
            int current = nums [i];
            int tempMax = max_so_far;

            max_so_far = Math.max(current, Math.max(current*max_so_far, current*min_so_far));
            min_so_far = Math.min(current, Math.min(current*tempMax, current*min_so_far));

            result = Math.max(result, max_so_far);
        }
        return result;
    }
}