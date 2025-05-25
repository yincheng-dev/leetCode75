class Solution {
    public int[] twoSum(int[] nums, int target) {
        //create a hash map
        HashMap<Integer,Integer> map = new HashMap<>();

        //loop through the array

        for (int i=0; i<nums.length;i++)
        {

            //calculate the number we need to find and save it as complement
            int complement= target - nums[i];
            //check if complement is in the map
            if(map.containsKey(complement)){
                //if yes, we found the pair
                // we return the index of the complement and the current i
                return new int[] {map.get(complement),i};
            
            }

            //if not, after each loop we store the current number and its index in the map

            map.put(nums[i],i);

        }
        //if no pair is found , return an empty array
        return new int []{};


    }
}