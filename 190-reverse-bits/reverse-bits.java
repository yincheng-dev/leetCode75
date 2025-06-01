public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result=0;

        // loop through all the 32 digits
        for ( int i = 0; i <32; i++ ){

            result <<= 1;
            result |= ( n & 1);
            n >>=1;
        }
        return result;
        // In 3 Steps 
        // 1. shift result to left to make room for next bit 
        // 2. get the last bit, and set it as result
        // 3. shift n right to process the next bit 
    }
}