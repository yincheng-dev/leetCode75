class Solution {
    public int maxProfit(int[] prices) {
        //two pointers , left and right
        int l =0;
        int r= 1;
        int maxP =0;
        
    while (r<prices.length){
        if (prices[r]>prices[l]){

         int profit=prices[r]-prices[l];
         maxP=Math.max(profit,maxP);

        }
        else {
            l=r;
        }
        r++;
    }
        
    
    return maxP;
}
}