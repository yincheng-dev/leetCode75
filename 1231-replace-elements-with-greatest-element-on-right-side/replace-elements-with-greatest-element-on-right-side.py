class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 1. set the maxRight to -1 bcs there is nothing right of the last element
        maxRight = -1

        # 2. loop backwards
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i] # save current value 
            arr[i] = maxRight # replace the current with max seen so far
            maxRight =max(temp,maxRight) # Update maxRight if needed

        return arr    


    
