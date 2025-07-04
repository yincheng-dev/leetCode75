class Solution(object):
    def coinChange(self, coins, amount):
        # Step 1 : Create a dp array 
        # dp [i] mans the minumal number of coin needed to make amount i
        dp = [amount+1]*(amount + 1)
        # Step 2 : initialize the amount 0, needed 0 coin
        dp[0]= 0 
        # Step 3 : Go through all amount from 1 to amount
        for x in range (1, amount + 1 ):  
          #step 4 : Try all coins 
          for coin in coins: 
            if x - coin >=0:
              #check if using this coin gives a better smaller result
              dp[x] = min (dp[x], dp [x-coin] +1)
        # Step 5: If we still have amount + 1, return -1 (not possible)      
        return dp[amount] if dp[amount]!= amount +1 else -1 


        